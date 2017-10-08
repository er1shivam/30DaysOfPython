from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "er05shivam@gmail.com"
from_email = username
password = "Ilove<3mymom5."
to_email = "er1shivam@gmail.com"

try:
    email_conn = smtplib.SMTP(host,port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username,password)

    the_msg = MIMEMultipart("alternative")
    the_msg['Subject'] = "Hello there!"
    the_msg['From'] = from_email

    plain_txt = "Testing the message"
    html_txt = """\
    <html>
        <head></head>
        <body>
            <p>Hey!<br/>
                Testing this email <b>message</b> <br/>
            </p>
            <p>
                From <a href="www.shivamsrivastava.me">Shivam</a>
            </p>
        </body>
    </html>
    """
    part_1 = MIMEText(plain_txt,'plain')
    part_2 = MIMEText(html_txt,"html")

    the_msg.attach(part_1)
    the_msg.attach(part_2)

    email_conn.sendmail(from_email,to_email, the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("Error sending message")