import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import datetime
import locale
from email.mime.base import MIMEBase
from email import encoders
from email.utils import COMMASPACE, formatdate

# Create variable with time (version 'pl')
locale.setlocale(locale.LC_TIME, 'pl')
time = datetime.datetime.now().strftime("%d %B %Y")

# Variables needed for changes in TemplateOfMail
welcome = "Dzień dobry Pani Marto,"
textOfParagraph = 'W nawiązaniu do rozmowy  telefonicznej'

# setting the necessary variables
send_from = 'emilialechart@wp.pl'
send_to = ['marek.baranski@interia.pl', 'maro.baranski@gmail.com']
send_cc = []
send_bcc = []
subject = 'test'
filesToAttach = ['c:/Users/Marek/Desktop/6-7.pdf', 'c:/Users/Marek/Desktop/6-8.pdf']
toaddrs = send_to

# function needed to connect with mail (hidden password)
print(send_from)
password = getpass.getpass()

# Replace the target string
with open('TemplateOfMail.html', 'r', encoding='utf-8') as file:
    filedata = file.read()

filedata = filedata.replace('time', time)
filedata = filedata.replace('textOfParagraph', textOfParagraph)
filedata = filedata.replace('welcome', welcome)

# Write the file out again
with open('ReadyMail.html', 'w', encoding='utf-8') as file:
    file.write(filedata)


# combination all of addresses needed to send an e-mail
def checkAddressees():
    if not send_cc and send_bcc:
        return send_to + send_bcc
    if not send_bcc and send_cc:
        return send_to + send_cc
    if not send_bcc and not send_cc:
        return send_to
    else:
        return send_to + send_cc + send_bcc


# The main function for sending an e-mail
def send_mail(server="localhost"):
    assert type(send_to) == list
    assert type(send_cc) == list
    assert type(send_bcc) == list
    assert type(filesToAttach) == list

    # server startup and logging into e-mail
    server.starttls()
    server.login(send_from, password)

    # a loop to send an e-mail - only one address is shown in "To:"
    for eachMail in toaddrs:
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = '%s\r\n' % eachMail
        msg['cc'] = '%s\r\n' % COMMASPACE.join(send_cc)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        # attaching an HTML template for sending an e-mail#
        with open("ReadyMail.html", "r", encoding='utf-8') as f:
            html = f.read()
        msg.attach(MIMEText(html, 'html'))

        # attaching all of attachment from list filesToAttach
        for f in filesToAttach:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(f, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
            msg.attach(part)

        # sending an e-mail to every address in the send_to list
        server.sendmail(send_from, eachMail, msg.as_string())

    # closing the connection with the server
    server.close()


# starting the function
send_mail(server=smtplib.SMTP('smtp.wp.pl', 587))

print('wiadomość została wysłana do:')
print(checkAddressees())
