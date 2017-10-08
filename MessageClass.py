import datetime

class MessageUser():
    user_details = []
    message = []
    base_message = """Hi {name}!

    Thank you for the purchase on {date}.
    We hope you are excited about using it.
    Just as a reminder the purchase total was ${total}.
    Have a great one!

    Team CodeForLife
    """
    def add_user(self,name,amount,email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f".%(amount)
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
                self.message.append(new_msg)
            return self.message
        return []



obj = MessageUser()
obj.add_user("shivam",455.5)
obj.add_user("Rahul",125.34)

print(obj.get_details())
print(obj.make_message())