from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from collections import deque

from app.services.access_policy import (
    describe_access,
    describe_restricted_access,
    has_module_access,
    normalize_role,
)
from app.services.groq_service import classify_query, format_answer, generate_answer, refine_question
from app.services.smart_query_service import get_relevant_templates, execute_smart_query
from app.services.embedder import get_embedding
from app.services.qdrant_service import search_data_filtered

router = APIRouter()

# Conversation history store: keyed by office_id, stores last 2 exchanges
# Each exchange = {"question": str, "answer": str}
conversation_history: dict[int, deque] = {}

# Keywords to detect data questions (exam, hostel, trainee topics)
DATA_KEYWORDS = {
    "exam", "marks", "mark", "result", "pass", "passed", "fail", "failed",
    "score", "scores", "subject", "grade", "grades",
    "hostel", "room", "warden", "bed", "allocation",
    "trainee", "trainees", "student", "students", "traine", "trianee", "trainne",
    "attendance", "present", "absent", "leave",
    "top", "highest", "lowest", "average", "total", "count",
    "performer", "percentage", "occupancy", "complaint", "schedule",
    "joined", "joining", "course", "department", "designation",
    "nominee", "calendar", "re-exam", "reexam",
    "building", "overcrowded", "vacant", "available", "empty", "unused",
    "male", "female", "ladies", "gender",
    "compare", "comparison", "vs", "versus", "improvement",
    "how many", "who", "which", "list", "show", "what", "detail", "details",
    "name", "email", "phone", "contact",
}

ACCESS_KEYWORDS = {"access", "permission", "permissions", "allowed", "role"}


class ChatRequest(BaseModel):
    message: str
    role: str = "principal"
    office_id: int = 1


def _is_data_question(message: str) -> bool:
    """Check if the message is asking about data/analytics (exam, hostel, trainee)."""
    text = message.lower()
    return any(kw in text for kw in DATA_KEYWORDS)


def _is_access_question(message: str) -> bool:
    text = message.lower()
    return any(kw in text for kw in ACCESS_KEYWORDS)


def _check_module_access(message: str, user_role: str) -> str | None:
    """Returns an error message if user lacks access, or None if OK."""
    text = message.lower()
    exam_words = {"exam", "marks", "mark", "result", "pass", "fail", "score", "grade", "subject"}
    hostel_words = {"hostel", "room", "bed", "building", "warden", "allocation"}

    if any(w in text for w in exam_words) and not has_module_access(user_role, "exam"):
        return "You do not have permission to access exam data."
    if any(w in text for w in hostel_words) and not has_module_access(user_role, "hostel"):
        return "You do not have permission to access hostel data."
    return None


def _qdrant_fallback(question: str, office_id: int, user_role: str) -> str | None:
    """Search Qdrant for relevant context and generate an answer.
    Returns the answer string, or None if no relevant results found."""
    import re

    try:
        vector = get_embedding(question)
        results = search_data_filtered(
            vector=vector,
            office_id=office_id,
            user_role=user_role,
            limit=1000,
        )

        if not results:
            return None

        # Keyword-based reranking to solve Vector DB's exact-match flaw
        clean_q = re.sub(r"'s\b", "", question.lower())
        query_words = set(re.findall(r'\b\w{3,}\b', clean_q))

        def score_chunk(r):
            text = r.payload.get("text", "").lower()
            return sum(1 for w in query_words if w in text)

        # Sort by keyword match score (descending), then original vector score
        results.sort(key=lambda r: (score_chunk(r), r.score), reverse=True)

        # Take only the top 15 most relevant chunks
        best_results = results[:15]

        # Check if top result is actually relevant (has keyword overlap)
        top_kw_score = score_chunk(best_results[0]) if best_results else 0
        top_vec_score = best_results[0].score if best_results else 0

        # If no keyword overlap AND low vector similarity, skip
        if top_kw_score == 0 and top_vec_score < 0.70:
            return None

        context = "\n".join([r.payload.get("text", "") for r in best_results])
        return generate_answer(question, context)
    except Exception:
        return None


def _format_to_html(text: str) -> str:
    """Enforces HTML formatting for the frontend."""
    import re
    # If text already contains HTML table, preserve it as-is
    if '<table' in text.lower():
        return text
    # Convert markdown bold to HTML bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Convert markdown newlines/bullets to HTML breaks
    text = text.replace('\n- ', '<br><b>•</b> ')
    text = text.replace('\n', '<br>')
    # Fix double breaks
    text = text.replace('<br><br>', '<br>')
    return text

@router.post("/chat")
def chat(request: ChatRequest):
    try:
        user_message = request.message.strip()
        user_role = normalize_role(request.role)
        office_id = request.office_id

        # Get or create conversation history for this office
        if office_id not in conversation_history:
            conversation_history[office_id] = deque(maxlen=2)
        history = list(conversation_history[office_id])

        # Helper to store exchange and return response
        def _respond(answer_text: str) -> dict:
            conversation_history[office_id].append({
                "question": user_message,
                "answer": answer_text
            })
            return {"type": "text", "message": _format_to_html(answer_text)}

        # --- Access questions (role/permission queries) ---
        if _is_access_question(user_message):
            lowered = user_message.lower()
            if "not access" in lowered or "cannot access" in lowered or "can't access" in lowered:
                return _respond(describe_restricted_access(user_role))
            return _respond(describe_access(user_role))

        # --- General / greeting questions (no data needed) ---
        if not _is_data_question(user_message):
            # Check if this might be a follow-up answer (e.g. user just typed "Transportation")
            # If history exists and last answer was a follow-up question, treat as data question
            is_followup = False
            if history:
                last_answer = history[-1].get("answer", "").lower()
                followup_signals = ["which course", "which exam", "please specify", "please provide", "which trainee", "can you provide", "please select", "select one"]
                if any(sig in last_answer for sig in followup_signals):
                    is_followup = True
            
            if not is_followup:
                qdrant_answer = _qdrant_fallback(user_message, office_id, user_role)
                if qdrant_answer:
                    return _respond(qdrant_answer)
                return _respond(generate_answer(user_message, ""))

        # --- Direct trainee selection handler (bypass AI) ---
        # If the previous answer was a TRAINEE_SELECT prompt and user clicked a name with Code
        if history:
            import re
            last_answer_raw = history[-1].get("answer", "")
            if "please select one" in last_answer_raw.lower():
                # Try to extract user_code first (e.g. "Alpa Mayank Talati (Code: U00939)" or just "U00939")
                code_match = re.search(r'\b([A-Z]\d{3,})\b', user_message.upper())
                if code_match:
                    user_code = code_match.group(1)
                    result = execute_smart_query("MARKS_OF_ONE_TRAINEE", {"user_code": user_code}, office_id)
                    if result and not result.startswith("Error"):
                        # If result contains HTML table, bypass format_answer to preserve it
                        if result.strip().startswith("<") and "<table" in result.lower():
                            return _respond(result)
                        formatted = format_answer(f"exam marks for trainee code {user_code}", result)
                        return _respond(formatted)
                # Fallback: try to extract numeric trainee_id
                id_match = re.search(r'\b(\d+)\b', user_message)
                if id_match:
                    trainee_id = int(id_match.group(1))
                    result = execute_smart_query("MARKS_OF_ONE_TRAINEE", {"trainee_id": trainee_id}, office_id)
                    if result and not result.startswith("Error"):
                        # If result contains HTML table, bypass format_answer to preserve it
                        if result.strip().startswith("<") and "<table" in result.lower():
                            return _respond(result)
                        formatted = format_answer(f"exam marks for trainee ID {trainee_id}", result)
                        return _respond(formatted)


        # --- Data question: 3-stage LLM pipeline ---

        # Access control check BEFORE calling LLM
        access_err = _check_module_access(user_message, user_role)
        if access_err:
            return {"type": "text", "message": access_err}

        # Stage 1: Refine question (spell correct + clarify)
        refined = refine_question(user_message)

        # Stage 2: Classify query + extract params (with conversation history)
        allowed_queries = get_relevant_templates(refined)
        route = classify_query(refined, allowed_query_ids=allowed_queries, history=history)
        qid = route.get("query_id")
        params = route.get("params") or {}

        if qid and qid != "NONE":
            # Stage 2.5: Execute SQL
            result = execute_smart_query(qid, params, office_id)

            if result and not result.startswith("Error"):
                # Check if the result is a trainee selection prompt (multiple matches)
                if result.startswith("TRAINEE_SELECT\n"):
                    trainee_text = result.replace("TRAINEE_SELECT\n", "")
                    return _respond(trainee_text)

                # If result already contains HTML (like tables), skip LLM formatting to preserve it
                if result.strip().startswith("<") and "<table" in result.lower():
                    return _respond(result)

                # Stage 3: LLM formats the answer
                formatted = format_answer(refined, result)

                # Only enrich with Qdrant for specific trainee profile queries where SQL data might be shallow
                if qid in ("HOSTEL_TRAINEE_DETAILS", "HOSTEL_SEARCH_TRAINEE_BY_NAME") and len(formatted) <= 80:
                    qdrant_answer = _qdrant_fallback(refined, office_id, user_role)
                    if qdrant_answer and len(qdrant_answer) > len(formatted):
                        return _respond(qdrant_answer)
                
                return _respond(formatted)

        # --- Fallback: Vector search (Qdrant) ---
        qdrant_answer = _qdrant_fallback(refined, office_id, user_role)
        if qdrant_answer:
            return _respond(qdrant_answer)

        # --- Final fallback: LLM with no context ---
        return _respond(generate_answer(refined, ""))

    except HTTPException as exc:
        return {"type": "text", "message": f"Error: {exc.detail if hasattr(exc, 'detail') else str(exc)}"}
    except Exception as exc:
        return {"type": "text", "message": f"Error: {exc}"}