import requests
from bs4 import BeautifulSoup
from pathlib import Path
import csv
from datetime import datetime

def get_apod_url(date_str):
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        formatted = dt.strftime("%y%m%d")
        return f"https://apod.nasa.gov/apod/ap{formatted}.html"
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        exit(1)

def download_apod(date_input):
    base_url = "https://apod.nasa.gov/apod/"
    page_url = get_apod_url(date_input)

    Path("images").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)

    res = requests.get(page_url)
    if res.status_code != 200:
        print("Page not found for this date.")
        return

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag = soup.find_all("b")[0]
    title = title_tag.text.strip() if title_tag else "No title"

    image_tag = soup.find("img")
    image_url = base_url + image_tag["src"] if image_tag else None

    explanation_paragraphs = soup.find_all("p")
    explanation = explanation_paragraphs[2].text.strip() if len(explanation_paragraphs) >= 3 else "No explanation"

    if image_url:
        image_data = requests.get(image_url).content
        image_name = image_url.split("/")[-1]
        image_path = Path("images") / image_name
        with open(image_path, "wb") as f:
            f.write(image_data)
        print(f"Image downloaded: {image_name}")
    else:
        image_name = "N/A"
        print("No image found.")

    metadata_file = Path("data") / "metadata.csv"
    write_header = not metadata_file.exists()
    with open(metadata_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["Date", "Title", "Image Name", "Explanation"])
        writer.writerow([date_input, title, image_name, explanation])

    print("Metadata saved to data/metadata.csv")

if __name__ == "__main__":
    date_input = input("Enter a date (YYYY-MM-DD): ")
    download_apod(date_input)
