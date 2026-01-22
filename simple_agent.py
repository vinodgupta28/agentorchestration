from google import genai
import os

class SimpleAgent:
    def __init__(self, role_prompt: str):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not set")

        self.client = genai.Client(api_key=api_key)
        self.role_prompt = role_prompt
        self.model = "models/gemini-flash-latest"

    def run(self, input_text: str) -> str:
        prompt = f"{self.role_prompt}\n\n{input_text}"
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text
