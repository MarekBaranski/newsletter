import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
import datetime
import locale
from email.mime.base import MIMEBase
from email import encoders

locale.setlocale(locale.LC_TIME, 'pl')
time = datetime.datetime.now().strftime("%d %B %Y")
welcome = "Dzień dobry Pani Marto,"
textOfParagraph = 'W nawiązaniu do rozmowy  telefonicznej'

email_user = 'emilialechart@wp.pl'
email_send = 'marek.baranski@interia.pl'

print(email_user)
password = getpass.getpass()

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = 'Portfolio Emilia Lech Barańska'

with open('TemplateOfMail.html', 'r', encoding='utf-8') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('time', time)
filedata = filedata.replace('textOfParagraph', textOfParagraph)
filedata = filedata.replace('welcome', welcome)

# Write the file out again
with open('ReadyMail.html', 'w', encoding='utf-8') as file:
    file.write(filedata)

# body = 'This is body of E-Mail'
report_file = open('ReadyMail.html', encoding='utf-8')
html = report_file.read()

# msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEText(html, 'html'))

# attachment
# filename = 'image.jpg'
# attachment = open(filename, 'rb')

# part = MIMEBase('aplication', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= "+filename)

# msg.attach(part)
textOfParagraph = msg.as_string()

server = smtplib.SMTP('smtp.wp.pl', 587)
server.starttls()
server.login(email_user, password)

server.sendmail(email_user, email_send, msg.as_string())
server.quit()
