from twilio.rest import Client

class smsSender:
    def __init__(self, id, auth_token, from_number):

        self.user = Client(id, auth_token)

        self.from_number = from_number


    def sendMessage(self, to_number, messageBody):
        message = self.user.messages.create(
            to=to_number,
            from_=self.from_number,
            body=messageBody
        )

        # print(message.id)



# Details of Account . Account Id and Auth Token & Twilio Number

account_sid = ''  # add Account ID
auth_token = '' # Auth Token
from_num = '' # Twilio Number


# Object of Class (Sender )
sender = smsSender(account_sid, auth_token, from_num)


# Message and Number
to_num = ' ' # Receivers Number
message = 'Your Text Message Goes here!'

sender.sendMessage(to_num, message)
