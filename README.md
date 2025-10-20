# 🧠 Python Automation Starter (GitHub Codespace Version)

A simple web scraping project built inside **GitHub Codespaces** using:
- Python 3
- BeautifulSoup4
- Requests
- Selenium (optional for automation)

## 🚀 Run in Codespaces
1. Open this repo in Codespaces.

python3 -m pip install --upgrade pip


2.Install Chromium in Codespace


sudo apt-get update
sudo apt-get install -y chromium-browser


If that fails (on some Codespaces images), try the fallback:

sudo apt-get install -y chromium


3. Install dependencies (auto via `requirements.txt`).
pip install -r requirements.txt

and Verify installations
python3 -m pip list




4. Run the project:Run the Selenium Scraper
   ```bash
   python3 main.py

5.Run the Streamlit Dashboard
streamlit run dashboard.py


⚙️ Codespace Chrome Setup (if Selenium fails)

If you get this error:

WebDriverException: Message: 'chromedriver' executable needs to be in PATH


Run these commands:

sudo apt-get update
sudo apt-get install -y chromium-browser


Then update your scraper.py:

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


## 🕒 Scheduled Runs & Email Reports

### 🔔 Email Summary Reports
After each run, the automation emails a summary report including:
- Total records scraped
- Sample data preview
- Timestamp

Configure your Gmail app password in `main.py` or `reporter.py`:
```python
send_summary_report(
    csv_path="data/scraped_data.csv",
    to_email="your_email@gmail.com",
    app_password="your_app_password"
)




python main.py
python scheduler.py



## 🧠 Streamlit Dashboard

To visualize the scraped data:

```bash
streamlit run dashboard.py
Then open the URL (Codespaces will show one).
You’ll see:

📄 Scraped data preview

🔍 Search & filter

💾 Download CSV

📊 Summary metrics## 🧠 Streamlit Dashboard

To visualize the scraped data:

```bash
streamlit run dashboard.py
Then open the URL (Codespaces will show one).
You’ll see:

📄 Scraped data preview

🔍 Search & filter

💾 Download CSV

📊 Summary metrics


---

Would you like me to **extend this dashboard** to include:
✅ domain-level charts (visual analytics)  
✅ a “Run Scraper” button that executes the automation from within the Streamlit UI?  
That would make it your **Level 4 full automation web app** (everything in one place).

