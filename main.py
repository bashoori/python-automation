# ------------------------------------------------------------
# 🧠 MAIN AUTOMATION SCRIPT WITH DASHBOARD
# ------------------------------------------------------------
# 1️⃣ Scrapes quotes from https://quotes.toscrape.com
# 2️⃣ Saves data to CSV
# 3️⃣ Sends summary email (using .env for credentials)
# 4️⃣ Launches a Streamlit dashboard to visualize data
# ------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import csv
import os
import pandas as pd
from dotenv import load_dotenv
from reporter import send_summary_report
import streamlit as st

# ✅ Load environment variables
load_dotenv()
TO_EMAIL = os.getenv("TO_EMAIL")


def scrape_quotes():
    """Scrape quotes and authors from the demo site and return a list of rows."""
    print("🌐 Fetching data from https://quotes.toscrape.com ...")

    URL = "https://quotes.toscrape.com/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    rows = [[quote.text, author.text] for quote, author in zip(quotes, authors)]

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


def generate_dashboard(file_path="data/quotes.csv"):
    """Generate a simple Streamlit dashboard to visualize scraped quotes."""
    df = pd.read_csv(file_path)
    st.set_page_config(page_title="Quotes Dashboard", page_icon="💬", layout="wide")

    st.title("💬 Quotes Dashboard")
    st.markdown("### Visualization of scraped data from [quotes.toscrape.com](https://quotes.toscrape.com)")

    st.dataframe(df, use_container_width=True)

    # Simple stats
    st.metric("Total Quotes", len(df))
    st.metric("Unique Authors", df["Author"].nunique())

    # Filter/search
    search_term = st.text_input("🔍 Search quotes or authors:")
    if search_term:
        filtered = df[df.apply(lambda r: search_term.lower() in r.astype(str).str.lower().to_string(), axis=1)]
        st.write(f"Results found: {len(filtered)}")
        st.dataframe(filtered)
    else:
        st.info("Type a keyword to search.")

    # Download button
    st.download_button(
        label="💾 Download CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="quotes.csv",
        mime="text/csv",
    )


def main():
    """Main function to scrape, save, email, and show dashboard."""
    try:
        rows = scrape_quotes()
        file_path = "data/quotes.csv"
        save_to_csv(rows, file_path)

        # 📧 Send summary report
        if TO_EMAIL:
            print("📧 Sending summary email...")
            send_summary_report(csv_path=file_path, to_email=TO_EMAIL)
        else:
            print("⚠️ No TO_EMAIL defined in .env — skipping email.")

        print("🎯 Data collected successfully — launching dashboard...")

        # 🚀 Run Streamlit dashboard
        # This works in Codespaces (interactive preview) or browser
        os.system("streamlit run main.py")  # Self-launch dashboard

    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
