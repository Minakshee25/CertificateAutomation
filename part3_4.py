import smtplib
import os
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg = EmailMessage()
msg['subject'] = 'IEEE CERTIFICATE'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'n.minakshee2000@gmail.com'

email_msg = open('email.html')
email_body = email_msg.read()

msg.set_content('This is a plain text email')
msg.add_alternative(email_body, subtype='html')
with open('butterfly.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)  # to find type of image import module imghdr
    file_name = 'IEEE certificate'

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()  # identifies server
    smtp.starttls()  # encrypt our traffic
    smtp.ehlo()  # reidentify as an encrypted connection

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
