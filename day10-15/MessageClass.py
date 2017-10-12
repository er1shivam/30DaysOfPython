import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


# Details to connect to the mail server using smtp

host = "smtp.gmail.com"
port = 587
username = "er05shivam@gmail.com"
from_email = username
password = "Ilove<3mymom5."
to_email = "er1shivam@gmail.com"

# using custom message predefined in message.html
file_html_ = "template\email_message.html"

class MessageUser():
    user_details = []
    message = []
    base_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it.
Just as a reminder the purchase total was ${total}.
Have a great one!

Team CodeForLife"""
    email_message = []
    def add_user(self,name,amount,email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f"%(amount)
        detail = {
            "name": name,
            "amount": amount,
        }
        today = datetime.date.today()
        date_text = '{today.day}/{today.month}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None:
            detail['email'] = email
        self.user_details.append(detail)

    def get_details(self):
        return self.user_details

    def make_message(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_mail = detail.get("email")
                if user_mail:
                    user_data = {
                        "email": user_mail,
                        "message": new_msg
                    }
                    self.email_message.append(user_data)
                else:
                    self.message.append(new_msg)
            return self.message
        return []
#       Method to send message
    def send_message(self):
        self.make_message()
        if len(self.email_message) > 0:
            for detail in self.email_message:
                user_email = detail["email"]
                user_message = detail["message"]

                try:
                    email_conn = smtplib.SMTP(host,port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username,password)

                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Hello there!"
                    the_msg["From"] = from_email
                    the_msg["To"] = user_email
                    part_1 = MIMEText(user_message,'plain')
                    the_msg.attach(part_1)

                    email_conn.sendmail(from_email,[user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("Error sending message")
            return True
        return False

    def premailmsg(self):
        for i in self.email_message:
            print(i)

obj = MessageUser()
obj.add_user("Shivam!",455.5,email='er3shivam@gmail.com')
obj.add_user("Shivam2",125.34,email='er1shivam@gmail.com')

# print(obj.get_details())
# print(obj.send_message())
