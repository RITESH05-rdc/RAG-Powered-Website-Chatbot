import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

visited = set()

def scrape_website(base_url, max_pages=10):

    to_visit = [base_url]

    while to_visit and len(visited) < max_pages:

        url = to_visit.pop(0)

        if url in visited:
            continue

        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "html.parser")

            text = soup.get_text()

            filename = f"data/pages/page_{len(visited)}.txt"

            with open(filename, "w", encoding="utf-8") as f:
                f.write(text)

            visited.add(url)

            for link in soup.find_all("a"):
                href = link.get("href")

                if href:
                    full_url = urljoin(base_url, href)

                    if base_url in full_url:
                        to_visit.append(full_url)

        except:
            pass