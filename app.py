import os
from langchain_groq import ChatGroq

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not set in environment")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.4,
        api_key=api_key
    )
