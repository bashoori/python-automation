import schedule
import time
import subprocess

def job():
    print("⏰ Running scheduled automation...")
    subprocess.run(["python3", "main.py"])

# Every 6 hours
schedule.every(6).hours.do(job)
# Or every day at 9 AM
# schedule.every().day.at("09:00").do(job)

print("🕒 Scheduler started. Waiting for next run...")
while True:
    schedule.run_pending()
    time.sleep(60)
