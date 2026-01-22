from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

class SimpleAgent:
    def __init__(self, role: str):
        self.role = role
        self.model = "models/gemini-flash-latest"

    def run(self, user_input: str) -> str:
        prompt = f"""
You are a {self.role}.

Task:
- Understand the topic
- Explain it clearly
- Use simple language
- Give examples if possible

User question:
{user_input}
"""
        response = client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text
