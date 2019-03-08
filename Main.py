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
from tkinter import messagebox


class BackendForApp:

    def __init__(self):
        # Create variable with time (version 'pl')
        locale.setlocale(locale.LC_TIME, 'pl')
        self.time = datetime.datetime.now().strftime("%d %B %Y")

        # Variables needed for changes in TemplateOfMail
        self.welcome = "Dzień dobry Pani Marto,"
        self.textOfParagraph = 'W nawiązaniu do rozmowy  telefonicznej'

        # setting the necessary variables
        self.send_from = 'emilialechart@wp.pl'
        self.send_to = []
        self.send_cc = []
        self.send_bcc = []
        self.subject = 'test'
        self.filesToAttach = []
        self.toaddrs = self.send_to

        # function needed to connect with mail (hidden password)
        self.server = smtplib.SMTP('smtp.wp.pl', 587)
        #print(self.send_from)
        self.password = 'biedronka1986'
        #self.password = getpass.getpass()

    def replaceHtml(self):
        # Replace the target string
        with open('TemplateOfMail.html', 'r', encoding='utf-8') as file:
            filedata = file.read()

        filedata = filedata.replace('time', self.time)
        filedata = filedata.replace('textOfParagraph', self.textOfParagraph)
        filedata = filedata.replace('welcome', self.welcome)

        # Write the file out again
        with open('ReadyMail.html', 'w', encoding='utf-8') as file:
            file.write(filedata)

    # combination all of addresses needed to send an e-mail
    def checkAddressees(self):
        if not self.send_cc and self.send_bcc:
            return self.send_to + self.send_bcc
        if not self.send_bcc and self.send_cc:
            return self.send_to + self.send_cc
        if not self.send_bcc and not self.send_cc:
            return self.send_to
        else:
            return self.send_to + self.send_cc + self.send_bcc

    # The main function for sending an e-mail
    def send_mail(self):
        assert type(self.send_to) == list
        assert type(self.send_cc) == list
        assert type(self.send_bcc) == list
        assert type(self.filesToAttach) == list

        # Replace proper field in HTML
        self.replaceHtml()

        # server startup and logging into e-mail
        self.server.starttls()
        self.server.login(self.send_from, self.password)

        # a loop to send an e-mail - only one address is shown in "To:"
        for eachMail in self.toaddrs:
            msg = MIMEMultipart()
            msg['From'] = self.send_from
            msg['To'] = '%s\r\n' % eachMail
            msg['cc'] = '%s\r\n' % COMMASPACE.join(self.send_cc)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = self.subject

            # attaching an HTML template for sending an e-mail#
            with open("ReadyMail.html", "r", encoding='utf-8') as f:
                html = f.read()
            msg.attach(MIMEText(html, 'html'))

            # attaching all of attachment from list filesToAttach
            for f in self.filesToAttach:
                part = MIMEBase('application', "octet-stream")
                part.set_payload(open(f, "rb").read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
                msg.attach(part)

            # sending an e-mail to every address in the send_to list
            self.server.sendmail(self.send_from, eachMail, msg.as_string())

        # closing the connection with the server
        self.server.close()

        messagebox.showinfo("Status wiadomości", "Wiadmość została wysłana :)")


# starting the function
#test_of_backend = BackendForApp()
#test_of_backend.send_mail()

#print('wiadomość została wysłana do:')
#print(test_of_backend.checkAddressees())
