import smtplib
import ssl
from email.message import EmailMessage

subject = "Email using Python"
body = "I am sending an email from python. I can't even believe this. This is honestly crazy."
sender_email = "alvin.nana@gmail.com"
receiver_email = "QuashieN@stanbic.com.gh"
password = input("Enter password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending email...")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Your Email has been successfully sent!")