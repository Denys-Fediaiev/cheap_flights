from twilio.rest import Client


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = "sid"
        self.token = "token"

    def send_message(self, send_data):
        client = Client(self.sid, self.token)
        message = client.messages.create(
            from_='+14406893664',
            body=send_data,
            to='+num'
        )
        print(message.sid)
