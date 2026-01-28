import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm():
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not set")

    return ChatGoogleGenerativeAI(
        model="models/gemini-flash-latest",
        temperature=0.4,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
