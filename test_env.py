import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

print("KEY =", os.getenv("AIzaSyCgH1b9tAENsJyP4J9FZB4NLNYfefOdgiw"))
