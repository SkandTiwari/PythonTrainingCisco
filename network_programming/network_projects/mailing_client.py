""" This demonstrate a simple mailing client using network programming """

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('network_programming\\network_projects\\pwd.txt', 'r') as f:
    password = f.read()

server.login('tiwariskand11@gmail.com', password)

msg = MIMEMultipart()
print(msg)
msg['From'] = 'Skand  Tiwari'
msg['to'] = 'tiwariskand11@gmail.com'
msg['Subject'] = 'test mail client'

with open('network_programming\\network_projects\\mail.txt', 'r') as file : 
    message = file.read()

msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
server.sendmail('tiwariskand11@gmail.com', 'tiwariskand11@gmail.com', text)
