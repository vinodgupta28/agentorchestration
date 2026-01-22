from google import genai
import os

# Read API key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

# Configure the client
client = genai.Client(api_key=API_KEY)

class SimpleAgent:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.model_name = "models/gemini-flash-latest"

    def run(self, input_text: str) -> str:
        # Combine system prompt + user input
        prompt = f"{self.system_prompt}\n\n{input_text}"

        # Generate content
        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )
        return response.text


# ===== Example usage =====
if __name__ == "__main__":
    agent = SimpleAgent("You are a helpful assistant.")
    result = agent.run("Say hello in one sentence")
    print("Response from Gemini API:")
    print(result)
