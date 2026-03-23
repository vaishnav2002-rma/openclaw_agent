import requests
from bs4 import BeautifulSoup


def search(query, num_results=5):
    url = f"https://html.duckduckgo.com/html/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    results = []
    for a in soup.select(".result__a", limit=num_results):
        link = a.get("href")
        if link:
            results.append(link)

    return results
