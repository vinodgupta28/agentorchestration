from google import genai

API_KEY = "AIzaSyCgH1b9tAENsJyP4J9FZB4NLNYfefOdgiw"

client = genai.Client(api_key=API_KEY)

# List all models
models = client.models.list()

print("Available models for your API key/project:")
for m in models:
    # Just print the name and description
    print(m.name, "-", getattr(m, "description", "No description"))
