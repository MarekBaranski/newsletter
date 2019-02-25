import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import datetime
import locale
from email.mime.base import MIMEBase
from email import encoders

# Create variable with time (version 'pl')
locale.setlocale(locale.LC_TIME, 'pl')
time = datetime.datetime.now().strftime("%d %B %Y")

# Variables needed for changes in TemplaeOfMail
welcome = "Dzień dobry Pani Marto,"
textOfParagraph = 'W nawiązaniu do rozmowy  telefonicznej'

# address of the sender and recipient
email_user = 'emilialechart@wp.pl'
email_send = 'marek.baranski@interia.pl'

# function needed to connect wth mail (hidden password)
print(email_user)
password = getpass.getpass()


# basic settings needed to send an e-mail

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = 'Portfolio Emilia Lech Barańska'

# Replace the target string
with open('TemplateOfMail.html', 'r', encoding='utf-8') as file:
    filedata = file.read()

filedata = filedata.replace('time', time)
filedata = filedata.replace('textOfParagraph', textOfParagraph)
filedata = filedata.replace('welcome', welcome)


# creating a new file to send to the client
with open('ReadyMail.html', 'w', encoding='utf-8') as file:
    file.write(filedata)

report_file = open('ReadyMail.html', encoding='utf-8')
html = report_file.read()

msg.attach(MIMEText(html, 'html'))


def add_attachment():
    filename = 'TemplateOfMail.html'
    attachment = open(filename, 'rb')
    part = MIMEBase('aplication', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)
    msg.attach(part)


# attachment
add_attachment()

# change content of e-mail to string
contentOfEmail = msg.as_string()


# connect with server SMPT and send e-mail
server = smtplib.SMTP('smtp.wp.pl', 587)
server.starttls()
server.login(email_user, password)
server.sendmail(email_user, email_send, contentOfEmail)
server.quit()
