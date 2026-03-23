from app.tools.search import search
from app.tools.scraper import scrape


def execute(action):
    if action.startswith("SEARCH"):
        query = action.replace("SEARCH", "").strip()
        return {"type": "search", "data": search(query)}

    elif action.startswith("OPEN"):
        url = action.replace("OPEN", "").strip()
        return {"type": "open", "data": scrape(url), "url": url}

    elif action.startswith("FINISH"):
        return {"type": "finish"}

    return {"type": "unknown"}
