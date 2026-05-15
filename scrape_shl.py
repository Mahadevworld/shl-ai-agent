import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

base_url = "https://www.shl.com/products/product-catalog/"

found = set()
assessments = []

for page in range(0, 30):

    url = f"{base_url}?start={page * 12}"

    print(f"Scraping page {page}...")
    print(url)

    response = requests.get(url, headers=headers)

    print("Status:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a")

    for link in links:

        text = link.get_text(strip=True)
        href = link.get("href")

        if (
            href
            and "/products/product-catalog/view/" in href
            and "solution" not in text.lower()
            and "job focused assessment" not in text.lower()
        ):

            full_url = "https://www.shl.com" + href

            if full_url not in found:

                found.add(full_url)

                assessments.append({
                    "name": text,
                    "url": full_url
                })

                print("Added:", text)

    time.sleep(1)

with open("shl_catalog.json", "w", encoding="utf-8") as file:
    json.dump(assessments, file, indent=4)

print("\nSaved", len(assessments), "assessments")