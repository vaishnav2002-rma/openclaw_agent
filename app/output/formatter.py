from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def format_output(memory, query):
    combined = "\n".join([m["data"] for m in memory])
    sources = [m["url"] for m in memory if "url" in m]

    prompt = f"""
Extract structured information about {query}.

DATA:
{combined}

Return STRICT JSON:
{{
  "name": "",
  "role": "",
  "companies": [],
  "background": "",
  "leadership_style": "",
  "key_events": [],
  "sources": {sources}
}}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    text = response.text.strip()

    try:
        return json.dumps(json.loads(text), indent=2)
    except:
        return text
