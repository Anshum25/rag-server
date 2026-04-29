import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def generate_answer(question: str, context: str) -> str:
    # Truncate context to avoid token limits
    if len(context) > 4000:
        context = context[:4000] + "\n...[truncated]"
    
    prompt = f"""You are TRMS AI Assistant. Give DIRECT, CONCISE answers based on the provided data.

CRITICAL RULES - YOU MUST FOLLOW THESE:
0. IF USER ASKS GREETINGS/NORMAL QUESTIONS (like "hey", "how are you", "bye") - answer naturally WITHOUT using any names from data
1. FOR DATA QUESTIONS: ONLY use information explicitly in the Context above. DO NOT hallucinate numbers, names, or facts.
2. If Context is empty or doesn't have the answer: Say "No data found for this query" - DO NOT make up an answer
3. Count ONLY what's in the context - don't guess totals
4. NEVER say "To find this..." or "Based on data..." - just answer directly
5. Use bullet points for lists: "- Item"
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