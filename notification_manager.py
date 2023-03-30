import os

from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = os.environ["AUTH_SID"]
        self.token = os.environ["TOKEN"]

    def send_message(self, send_data):
        client = Client(self.sid, self.token)
        message = client.messages.create(
            from_='+14406893664',
            body=send_data,
            to=os.environ["PHONE_NUM"]
        )
        print(message.sid)
