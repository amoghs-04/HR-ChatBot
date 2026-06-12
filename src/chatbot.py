import os
import google.generativeai as genai

from dotenv import load_dotenv
from src.retriever import retrieve_chunks

load_dotenv()

genai.configure(
    api_key=os.getenv("AQ.Ab8RN6Jgc1HizeD83QrG6UbMn0XERqC6-GSQnwA2CKkU6bxfDQ")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_answer(question, chat_history=""):

    # Use history for better retrieval
    retrieval_query = f"""
Conversation History:
{chat_history}

Current Question:
{question}
"""

    retrieved_chunks = retrieve_chunks(retrieval_query)

    if not retrieved_chunks:
        return (
            "I could not find relevant information in the provided knowledge source.",
            []
        )

    context = "\n\n".join(
        [chunk["text"] for chunk in retrieved_chunks]
    )

    prompt = f"""
You are Nineleaps HR Knowledge Assistant.

STRICT RULES:

1. Use conversation history to understand follow-up questions.
2. Answer ONLY from provided context.
3. Never use outside knowledge.
4. If answer is not found say:
'I could not find relevant information in the provided knowledge source.'
5. Company name is Nineleaps.
6. Keep answers concise.
7. If user asks:
   - "it"
   - "that"
   - "this policy"
   - "that policy"
   
   use Conversation History to understand what they are referring to.

Conversation History:
{chat_history}

Context:
{context}

Current Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    sources = list(
        set(
            [
                f"Nineleaps HR Policy Manual - Page {chunk['page']}"
                for chunk in retrieved_chunks
            ]
        )
    )

    return response.text, sources