# ------------------------------------------------------------
# 🧠 MAIN AUTOMATION SCRIPT
# ------------------------------------------------------------
# This script:
# 1️⃣ Scrapes quotes and authors from https://quotes.toscrape.com
# 2️⃣ Saves them to data/quotes.csv
# 3️⃣ Sends an email summary report (using .env for security)
# ------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import csv
import os
from dotenv import load_dotenv
from reporter import send_summary_report  # custom summary report email script

# ✅ Load environment variables (email credentials)
load_dotenv()
TO_EMAIL = os.getenv("TO_EMAIL")


def scrape_quotes():
    """Scrape quotes and authors from the demo site and return a list of rows."""
    print("🌐 Fetching data from https://quotes.toscrape.com ...")

    URL = "https://quotes.toscrape.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Extract all quotes and authors
    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    rows = []
    for quote, author in zip(quotes, authors):
        rows.append([quote.text, author.text])

    print(f"✅ Found {len(rows)} quotes.")
    return rows


def save_to_csv(rows, file_path="data/quotes.csv"):
    """Save scraped data into a CSV file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Quote", "Author"])
        writer.writerows(rows)
    print(f"💾 Data saved to {file_path}")


def main():
    """Main function that runs the scraping + email summary."""
    try:
        # 1️⃣ Scrape quotes
        rows = scrape_quotes()

        # 2️⃣ Save data to CSV
        file_path = "data/quotes.csv"
        save_to_csv(rows, file_path)

        # 3️⃣ Send summary email
        if TO_EMAIL:
            print("📧 Sending summary email...")
            send_summary_report(csv_path=file_path, to_email=TO_EMAIL)
        else:
            print("⚠️ No TO_EMAIL defined in .env — skipping email report.")

        print("🎯 Automation run complete.")

    except Exception as e:
        print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
