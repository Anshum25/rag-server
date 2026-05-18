import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def classify_query(question: str, allowed_query_ids: list, history: list = None) -> dict:
    import datetime
    current_year = datetime.datetime.now().year
    
    # Build conversation history context
    history_context = ""
    if history:
        history_lines = []
        for h in history:
            history_lines.append(f"User: {h['question']}")
            # Truncate long answers to save tokens
            answer = h['answer'][:200] + "..." if len(h['answer']) > 200 else h['answer']
            history_lines.append(f"Assistant: {answer}")
        history_context = f"""
Conversation History (last {len(history)} exchange(s)):
{chr(10).join(history_lines)}
"""
    
    prompt = f"""You are a query router for TRMS (TRAINING RESOURCE MANAGEMENT SYSTEM).
Current Date/Year Context: {datetime.datetime.now().strftime('%Y-%m-%d')}

Task: Choose exactly ONE query_id from the allowed list and extract parameters from the user's question.
IMPORTANT: If the user's current question is a follow-up or continuation of the conversation history, combine context from the history with the current question to determine the correct query_id and parameters. For example, if the previous question was "top performers" and the AI asked "which exam?" and the user now says "Transportation", extract course_name: "Transportation" and use the query_id from the previous context.

Allowed queries (each has id and description with expected params):
{json.dumps(allowed_query_ids)}

Return STRICT JSON ONLY:
{{"query_id": "...", "params": {{...}} }}
{history_context}
Parameter extraction rules:
- year: Extract any 4-digit year mentioned (e.g. "in 2025" → "year": 2025). Do NOT hallucinate a year if not explicitly stated, except when calculating relative to the current year.
- month: Extract month number (1-12) ONLY if a TEXT NAME of a month (like January, December) is explicitly used. NEVER extract this if the user says "last 12 months" or similar.
- start_month: Extract starting month number if a range is given (e.g. "between January..." -> 1).
- end_month: Extract ending month number if a range is given (e.g. "...to December" -> 12).
- last_months: Extract number of months if user says "last X months" (e.g. "last 4 months" -> 4, "last 12 months" -> 12).
- last_years: Extract number of years if user says "last X years" or "last year" (e.g. "last year" -> 1). NEVER extract this if the user uses the word "months".
- limit: Extract count if user says "top 5" or "top 20" etc (default 10)
- threshold_pct: Extract percentage if user says "below 50%" (default 40)
- search_name: Extract trainee name if mentioned
- building_name: Extract building/hostel name if mentioned
- room_name: Extract room number if mentioned
- gender: Extract "male" or "female" if mentioned
- trainee_id: Extract numeric ID if mentioned
- min_failures: Extract minimum failure count if mentioned (default 2)
- course_name: Extract ONLY the actual training course or program name if mentioned (e.g. "Establishment exam" -> "Establishment", "Cabinman course" -> "Cabinman"). NEVER extract generic words like "exam", "performers", "marks", "course", "top", "highest", "lowest" as course_name. If no specific course/program name is mentioned, do NOT include course_name at all.
- year1, year2: Extract two years for comparison queries

Rules:
1) Match if the user's intent clearly corresponds to the meaning. Even if the phrasing is different (e.g. "how many" vs "total"), pick the most relevant query_id. If the user asks for unstructured details NOT related to these queries (like "remarks", "building codes", "phone numbers", or broad "summaries"), you MUST return: {{"query_id": "NONE", "params": {{}}}}
2) If you are unsure, always default to {{"query_id": "NONE", "params": {{}}}}
3) Do NOT include explanations, only JSON.
4) Extract ALL relevant parameters from the question.

User question:
{question}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        content = (response.choices[0].message.content or "").strip()
        # Best-effort JSON parse (model sometimes wraps with ```json)
        content = content.replace("```json", "").replace("```", "").strip()
        parsed = json.loads(content)
        if not isinstance(parsed, dict):
            return {"query_id": "NONE", "params": {}}
        query_id = parsed.get("query_id")
        params = parsed.get("params")
        
        # Validating query_id exists if it's a list of strings or dicts
        allowed_set = set()
        for item in allowed_query_ids:
            if isinstance(item, dict):
                allowed_set.add(item.get("id"))
            else:
                allowed_set.add(item)
                
        if query_id not in allowed_set.union({"NONE"}):
            return {"query_id": "NONE", "params": {}}
        if not isinstance(params, dict):
            params = {}
        return {"query_id": query_id, "params": params}
    except Exception:
        return {"query_id": "NONE", "params": {}}


def refine_question(question: str) -> str:
    prompt = f"""You are a text-only question refiner.

Task:
- Correct spelling and rewrite the question into a clear, standard English query.
- Preserve the original intent exactly.
- Do NOT add new constraints, names, numbers, years, or assumptions.
- Do NOT answer the question.

Output rules:
- Return ONLY the refined question as plain text.
- No quotes, no markdown, no explanations.

User question:
{question}

Refined question:
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return (response.choices[0].message.content or "").strip()
    except Exception:
        return question


def generate_answer(question: str, context: str) -> str:
    # Truncate context to avoid token limits (Groq free tier is ~6000 TPM limit, ~20k chars)
    if len(context) > 14000:
        context = context[:14000] + "\n...[truncated]"
    
    import datetime
    prompt = f"""You are TRMS (TRAINING RESOURCE MANAGEMENT SYSTEM) AI Assistant. Give DIRECT, CONCISE answers based on the provided data.
Current Date/Year Context: {datetime.datetime.now().strftime('%Y-%m-%d')}

CRITICAL RULES - YOU MUST FOLLOW THESE:
0. STRICT DOMAIN RESTRICTION: You are exclusively a TRMS assistant. If the user asks a general knowledge question NOT related to TRMS, trainees, exams, results, marks, schedules, hostels, courses, batches, or your identity (e.g., "how to make coffee", coding questions, math, trivia, weather), you MUST reply: "I am a TRMS assistant and can only answer questions related to the Training Resource Management System."
1. FOR DATA QUESTIONS: ONLY use information explicitly in the Context above. DO NOT hallucinate numbers, names, or facts.
2. If Context is empty and it is clearly a DATA QUESTION about TRMS, say "I do not have access to that specific data at the moment." You may answer basic greetings ("hi", "who are you") naturally.
3. Count ONLY what's in the context - don't guess totals
4. NEVER say "To find this..." or "Based on data..." - just answer directly
5. FORMATTING IS CRITICAL: The frontend requires HTML. NEVER use markdown (** or -). Use <b> for keys (e.g., <b>Name:</b> Value). Use <br> for every line break. Put a <br> after every single field so it displays as a vertical list.
7. Return ONLY the answer text. NEVER prefix the response with "Response:", "Answer:", or any other label.
8. Start the answer immediately with the content.

Context:
{context}

User question:
{question}

Direct Answer:
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating answer: {str(e)}"

    
def format_answer(question: str, result_context: str) -> str:
    if len(result_context) > 6000:
        result_context = result_context[:6000] + "\n...[truncated]"

    import datetime
    prompt = f"""You are TRMS (TRAINING RESOURCE MANAGEMENT SYSTEM) AI Assistant.
Current Date/Year Context: {datetime.datetime.now().strftime('%Y-%m-%d')}

You will be given a User question and a RESULT CONTEXT produced by SQL.

CRITICAL RULES:
1) Use ONLY the RESULT CONTEXT. Do not add any new facts.
2) Do NOT change numbers, names, dates, or counts. Repeat them exactly as in RESULT CONTEXT.
3) If RESULT CONTEXT indicates no data, explain why briefly (e.g. "I found the trainee but they have no exam records" or "No records found for that name in your office"). Do NOT just say "No data found".
4) Keep it short and direct.
5) Return ONLY the answer text. NEVER prefix the response with "Response:", "Answer:", or any other label.
6) Start the answer immediately with the content.
7) NEVER use introductory filler phrases like "Based on the RESULT CONTEXT" or "It appears that".
8) NEVER analyze the completeness of the data. If the RESULT CONTEXT contains ANY records matching the user's criteria, simply list them exactly as provided.
9) If the RESULT CONTEXT provides a 'Total' count AND a list, you MUST include BOTH the total count and the list in your final answer. Do NOT drop the count.
10) NEVER include internal database IDs like user_id, trainee_id, application_id, office_id, etc. Only show human-readable information like name, marks, course name, dates.
11) Answer naturally without showing internal column names. For example, say "John scored 95 marks" instead of showing "name: John, marks: 95".

RESULT CONTEXT:
{result_context}

User question:
{question}

Final Answer:
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating answer: {str(e)}"