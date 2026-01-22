from google import genai

# 🔑 Your API key here
API_KEY = "AIzaSyCgH1b9tAENsJyP4J9FZB4NLNYfefOdgiw"

# Initialize client
client = genai.Client(api_key=API_KEY)

# Generate text using a valid model
response = client.models.generate_content(
    model="models/gemini-2.5-flash",  # ✅ Use one of the models from list_models.py
    contents="Say hello in one sentence"
)

# Print the generated text
print("Response from Gemini API:")
print(response.text)
