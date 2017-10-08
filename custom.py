import smtplib

host = "smtp.gmail.com"
port = 587
username = "er05shivam@gmail.com"
password = "Ilove<3mymom5."

from_email = username
to_list = ["er1shivam@gmail.com"]

email_conn = smtplib.SMTP(host,port)

email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_email,to_list,"Hello \n this is a message demo.")

email_conn.quit()