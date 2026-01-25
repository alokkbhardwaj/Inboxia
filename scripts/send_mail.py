import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "demo@project.com"
msg["To"] = "student@project.com"
msg["Subject"] = "SMTP Project Final Demo"
msg.set_content("Final working demo: Python → Postfix → Inboxia")

with smtplib.SMTP("localhost", 587) as server:
    server.send_message(msg)

print("✅ FINAL DEMO MAIL SENT")
