import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def classify_query(question: str, allowed_query_ids: list) -> dict:
    prompt = f"""You are a query router for TRMS (TRAINING RESOURCE MANAGEMENT SYSTEM).

Task: Choose exactly ONE query_id from the allowed list and extract parameters from the user's question.

Allowed queries (each has id and description with expected params):
{json.dumps(allowed_query_ids)}

Return STRICT JSON ONLY:
{{"query_id": "...", "params": {{...}} }}

Parameter extraction rules:
- year: Extract any 4-digit year mentioned (e.g. "in 2024" → "year": 2024)
- limit: Extract count if user says "top 5" or "top 20" etc (default 10)
- threshold_pct: Extract percentage if user says "below 50%" (default 40)
- search_name: Extract trainee name if mentioned
- building_name: Extract building/hostel name if mentioned
- room_name: Extract room number if mentioned
- gender: Extract "male" or "female" if mentioned
- trainee_id: Extract numeric ID if mentioned
- min_failures: Extract minimum failure count if mentioned (default 2)
- year1, year2: Extract two years for comparison queries

Rules:
1) ONLY match if the question perfectly aligns with the description. If the user asks for unstructured details NOT mentioned in the description (like "remarks", "building codes", "phone numbers", or broad "summaries"), you MUST return: {{"query_id": "NONE", "params": {{}}}}
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
    
    prompt = f"""You are TRMS (TRAINING RESOURCE MANAGEMENT SYSTEM) AI Assistant. Give DIRECT, CONCISE answers based on the provided data.

CRITICAL RULES - YOU MUST FOLLOW THESE:
0. STRICT DOMAIN RESTRICTION: You are exclusively a TRMS assistant. If the user asks a general knowledge question NOT related to TRMS, trainees, hostels, or your identity (e.g., "how to make coffee", coding questions, math, trivia), you MUST reply: "I am a TRMS assistant and can only answer questions related to the Training Resource Management System."
1. FOR DATA QUESTIONS: ONLY use information explicitly in the Context above. DO NOT hallucinate numbers, names, or facts.
2. If Context is empty and it is clearly a DATA QUESTION about TRMS, say "I do not have access to that specific data at the moment." You may answer basic greetings ("hi", "who are you") naturally.
3. Count ONLY what's in the context - don't guess totals
4. NEVER say "To find this..." or "Based on data..." - just answer directly
5. FORMATTING IS CRITICAL: The frontend requires HTML. NEVER use markdown (** or -). Use <b> for keys (e.g., <b>Name:</b> Value). Use <br> for every line break. Put a <br> after every single field so it displays as a vertical list.
6. If asking about counts (how many): Count the actual records in context, don't estimate

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

    prompt = f"""You are TRMS (TRAINING RESOURCE MANAGEMENT SYSTEM) AI Assistant.

You will be given a User question and a RESULT CONTEXT produced by SQL.

CRITICAL RULES:
1) Use ONLY the RESULT CONTEXT. Do not add any new facts.
2) Do NOT change numbers, names, dates, or counts. Repeat them exactly as in RESULT CONTEXT.
3) If RESULT CONTEXT indicates no data, answer nicely like: "I couldn't find any specific records for this." Do NOT say "No data found for this query".
4) Keep it short and direct.
5) FORMATTING IS CRITICAL: The frontend requires HTML. NEVER use markdown (** or -). Use <b> for keys (e.g., <b>Name:</b> Value). Use <br> for every line break. Put a <br> after every single field so it displays as a vertical list.

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