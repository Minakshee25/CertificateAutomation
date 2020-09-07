import os
import pandas as pd
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
df = pd.read_csv('sample.csv')

pth = "C:/Users/naray/OneDrive/Desktop/IEEE/certficateautomation/pictures"

for i in os.listdir('./pictures'): #i=Name Surname.png
    for index,j in df.iterrows(): #j=row, index=index
        if os.path.splitext(i)[0].lower() == j['name'].lower():

            x = os.path.join(pth, i) #join pth and i(Name surname.png) x = C:/Users/naray/OneDrive/Desktop/IEEE/certficateautomation/pictures\Dashrath Narayankar.png
            print(x)
            print(j['mailid'])

            msg = EmailMessage()
            msg['subject'] = 'IEEE CERTIFICATE'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = j['mailid']

            msg.set_content('This is a plain text email')
            msg.add_alternative("""\
                <!DOCTYPE html>
                <html>
                    <body>
                        <h1 style="color:blue;">IEEE CERTIFICATE</h1>
                    </body>
                </html>
                """, subtype='html')

            with open(x, 'rb') as f:
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
