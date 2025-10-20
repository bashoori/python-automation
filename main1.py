from bs4 import BeautifulSoup
import requests
import csv

URL = "https://quotes.toscrape.com/"  # demo site for scraping
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

rows = []
for quote, author in zip(quotes, authors):
    rows.append([quote.text, author.text])

with open("data/quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])
    writer.writerows(rows)

print("✅ Scraping complete! Data saved to data/quotes.csv")
