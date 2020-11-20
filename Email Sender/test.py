import smtplib
import ssl

port = 465

sender = "your_email"
password = "your_password"

recieve = str(input('To: '))

message = str(input('Message: '))

context = ssl.create_default_context()

print("Starting to send")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)

print("sent email!")
