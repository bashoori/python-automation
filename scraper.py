from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os, time

def login_and_scrape():
    options = Options()

    # ✅ Headless mode for Codespaces
    options.add_argument("--headless=new")  # use new headless mode for Chrome 109+
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")
    options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    message = driver.find_element(By.TAG_NAME, "h1").text
    print(f"✅ Login result: {message}")

    links = [a.get_attribute("href") for a in driver.find_elements(By.TAG_NAME, "a") if a.get_attribute("href")]
    df = pd.DataFrame(links, columns=["Links"])
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/scraped_data.csv", index=False)

    driver.quit()
    print("✅ Headless scraping complete. Data saved to data/scraped_data.csv")

    return df
