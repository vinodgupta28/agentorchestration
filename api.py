from google import genai
import os

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not set in environment variables")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "models/gemini-flash-latest"


def run_agent(system_prompt: str, user_input: str) -> str:
    prompt = f"{system_prompt}\n\n{user_input}"

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text
