import os
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv

# Explicitly point to backend/.env regardless of where uvicorn is run from
env_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("DEBUG - Loaded key:", GEMINI_API_KEY[:10] if GEMINI_API_KEY else "NOT FOUND")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_content(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating content: {str(e)}"