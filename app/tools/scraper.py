import requests
from bs4 import BeautifulSoup


def scrape(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=5)

        soup = BeautifulSoup(res.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]

        text = " ".join(paragraphs[:20])
        return text[:3000]

    except Exception as e:
        return ""
