import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq



load_dotenv()

def get_llm():
    return ChatGroq(
        model_name="llama-3.1-8b-instant",
        temperature=0.4,
        api_key=os.getenv("GROQ_API_KEY")
    )
