import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# ✅ Load credentials from .env
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email_alert(subject, body, to_email):
    """Send a simple notification email using secure .env credentials."""
    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise ValueError("❌ Missing EMAIL_ADDRESS or EMAIL_PASSWORD in .env")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("📧 Email alert sent successfully!")
    except Exception as e:
        print(f"⚠️ Failed to send email: {e}")
