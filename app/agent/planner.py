from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def decide(context):
    prompt = f"""
You are an autonomous research agent.

Context:
{context}

Decide next action:

Options:
1. SEARCH <query>
2. OPEN <url>
3. FINISH

Rules:
- First SEARCH
- Then OPEN links
- After enough info, FINISH
- Output ONLY action

Example:
SEARCH Elon Musk biography
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text.strip()
