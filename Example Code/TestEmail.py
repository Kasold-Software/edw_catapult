import smtplib
from email.message import EmailMessage

from_address = 'noreply@massstreetuniversity.com'
to_address = 'bob@massstreet.net'
user_name = 'AKIAYOI2BDSSXQ5TWMF6'
password = 'BGArTGxeIrqCneDk0tnt2iLESZTD+xymln3pvAoVABkN'
smtp_server = 'email-smtp.us-east-1.amazonaws.com'
smtp_port = '465'


def send_exception_email(exchange_directory):
    msg = EmailMessage()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = 'Empty Directory In EOD Data'
    msg.set_content('There are no files in ' + exchange_directory)

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(user_name, password)
        server.send_message(msg)
        server.quit()
    except TimeoutError as e:
        print(str(e))

send_exception_email('this directory')