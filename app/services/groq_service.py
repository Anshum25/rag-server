import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")


def generate_answer(question: str, context: str) -> str:
    prompt = f"""You are TRMS AI Assistant, a professional but friendly AI assistant for a Training ResourceManagement System.

Your job:
- Help users understand TRMS data clearly.
- Answer in a helpful, natural tone.
- Use ONLY the provided context for data-specific answers.
- If the user greets you or asks casual questions, respond politely without needing context.
- If data is missing, say you do not have enough data, then suggest what data or report may be needed.
- Do not make up trainee names, marks, rooms, dates, or results.
- Keep answers clear and useful.
- For data answers, give slightly explanation, not just one sentence.
- End with a helpful follow-up suggestion when appropriate.
- If user asks about a specific person, only answer if exact name match is found in context
- Do not guess or generalize

Context:
{context}

User question:
{question}

Answer:
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