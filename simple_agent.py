from google import genai
import os

#  Use environment variable or hardcode for testing
API_KEY = os.getenv("AIzaSyCgH1b9tAENsJyP4J9FZB4NLNYfefOdgiw") 

# Configure the client
client = genai.Client(api_key=API_KEY)

class SimpleAgent:
    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt
        self.model_name = "models/gemini-flash-latest"  # ✅ correct model for generate_content

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
