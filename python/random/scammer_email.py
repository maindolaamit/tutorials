import string, json, random, os
# Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Import smtplib for the actual sending function
import smtplib


def send_mail(mail_to, mail_from, mail_subject, mail_body):
    # Create a text/plain message
    MSG = MIMEMultipart()

    MSG['Subject'] = mail_subject
    MSG['From'] = mail_from
    MSG['To'] = mail_to
    MSG.attach(MIMEText(mail_body, 'plain'))

    # Send the message via our own SMTP server, but don't include the envelope header.
    server = smtplib.SMTP(host="localhost")
    server.sendmail(MSG['From'], MSG['To'], MSG.as_string())
    server.quit()


chars = string.ascii_letters + string.digits + '@!#$'
random.seed = (os.urandom(1024))
print chars

os.chdir('D:\python_test')
names = json.loads(open('names.json').read())

for name in names:
    name_extra = ''.join(random.choice(string.digits))

    username = name.lower() + name_extra + '@utsav.com'
    password = ''.join(random.choice(chars) for i in range(8))
    mail_to = 'maindola.amit@gmail.com'
    print 'Sending email to %s from %s' % (mail_to, username)

    send_mail(mail_to, username, 'Hello', 'Hi')
