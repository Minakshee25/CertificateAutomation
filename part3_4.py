import os
import pandas as pd
import smtplib
from email.utils import make_msgid
import mimetypes
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
            msg['subject'] = 'Quantum Computing Webinar'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = j['mailid']

            image_cid = make_msgid(domain='xyz.com')

            msg.set_content('Thanks for attending workshop on Quantum Computing by Sameer Yerpude')
            msg.add_alternative("""\
                <!DOCTYPE html>
                <html>
                    <head>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    </head>
                    <body>
                        <h1>Greetings {name}</h1>
                        <p><b>Thanks for attending workshop on Quantum Computing by Sameer Yerpude</b></p>
                        <p><b>Kindly find your E-certificate for the same, attached along with this mail.<br>We look forward seeing you at all our future workshops, seminars and events!</b><p>
                        <p><b>Regards<br>IEEE-VIT Student Branch</b></p>
                        <div style="text-align:center">
                            <p><b>Connect with us on</b></p>
            
                            <a href="https://www.facebook.com/IEEEVIT1"><img src="https://www.bworldonline.com/wp-content/uploads/2020/08/f_logo_RGB-Hex-Blue_512.png" height="45" width="45"></img></a>
            
                            <a href="https://www.instagram.com/ieeevit/?hl=en"><img src="https://static01.nyt.com/images/2016/05/11/us/12xp-instagram/12xp-instagram-facebookJumbo-v2.jpg" height="55" width="100"></img></a>
            
                            <a href="https://ieee.vit.edu.in/"><img src="https://ieee.vit.edu.in/assets/images/ieeevit-blue-1-5017x1103.png" height="55" width="100"></img></a>
                            <p><b>Ask us anything about programming, meet like minded people, build projects.</b></p>
                            <p><b>Join the coders Republic Group now:</b></p>
                            <a href="https://chat.whatsapp.com/GNjVY5fSZav73fl77vGPj2"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/WhatsApp_logo-color-vertical.svg/600px-WhatsApp_logo-color-vertical.svg.png" height="50" width="50"></img></a>
                            <p><b>For any error in certificate <a>click here</a></b></p>
                        </div>
                        <img src="cid:{image_cid}">
                    </body>
                </html>
                """.format(name=j['name'],image_cid=image_cid[1:-1]), subtype='html')

            with open(x, 'rb') as img:
                file_data = img.read()
                maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
                msg.get_payload()[1].add_related(file_data, maintype=maintype, subtype=subtype, cid=image_cid)

            msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename='IEEE certificate')

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()  # identifies server
                smtp.starttls()  # encrypt our traffic
                smtp.ehlo()  # reidentify as an encrypted connection

                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

                smtp.send_message(msg)
