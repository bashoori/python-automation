import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv
import smtplib, os

load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_summary_report(csv_path, to_email):
    """Send a detailed summary report with sample data."""
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise ValueError("❌ Missing EMAIL_ADDRESS or EMAIL_PASSWORD in .env")

    df = pd.read_csv(csv_path)
    total_records = len(df)
    sample = df.head(5).to_string(index=False)

    subject = f"Automation Report – {total_records} Records"
    body = f"""
    ✅ Automation Summary Report

    Total Records: {total_records}

    Sample Data:
    {sample}

    🚀 Generated automatically from your GitHub Codespace.
    """

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 Summary email sent successfully!")
    except Exception as e:
        print(f"⚠️ Failed to send summary email: {e}")
