import smtplib
import ssl
from email.message import EmailMessage
from config import settings

def send_email_with_report(html_path, pass_count, fail_count):
    subject = f"🧪 Selenium Report: {pass_count} Passed / {fail_count} Failed"
    body = "Hi Team,\n\nPlease find the attached Selenium AI Report.\n\nRegards,\nAutomation Bot"

    msg = EmailMessage()
    msg["From"] = settings.EMAIL_SENDER
    msg["To"] = settings.EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.set_content(body)

    with open(html_path, "rb") as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype="text", subtype="html", filename="ai_selenium_report.html")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(settings.SMTP_SERVER, settings.SMTP_PORT, context=context) as smtp:
        smtp.login(settings.EMAIL_SENDER, settings.EMAIL_PASSWORD)
        smtp.send_message(msg)
