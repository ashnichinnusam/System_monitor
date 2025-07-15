import psutil
import smtplib
from email.mime.text import MIMEText

def send_email_alert(subject, body, to_email):
    from_email = "your.email@gmail.com"
    from_password = "your_app_password"  # Use your Gmail App Password here

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, from_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", e)

# Define thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 80  # in percent

def check_system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    if cpu > CPU_THRESHOLD:
        alert_msg = f"High CPU usage detected: {cpu}%"
        print("[ALERT]", alert_msg)
        send_email_alert("System Alert: CPU Usage", alert_msg, "receiver.email@example.com")

    if memory > MEMORY_THRESHOLD:
        alert_msg = f"High Memory usage detected: {memory}%"
        print("[ALERT]", alert_msg)
        send_email_alert("System Alert: Memory Usage", alert_msg, "receiver.email@example.com")

    if disk > DISK_THRESHOLD:
        alert_msg = f"Low Disk space detected: {disk}%"
        print("[ALERT]", alert_msg)
        send_email_alert("System Alert: Disk Space", alert_msg, "receiver.email@example.com")


if __name__ == "__main__":
    check_system()
