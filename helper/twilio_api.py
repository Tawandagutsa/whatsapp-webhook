import os

from twilio.rest import Client

account_sid = 'ACb467aa16c4499bf8d0866105b07417dd'
auth_token = 'dd8b1ca2e094f2647de9fabd7c8bae73'
client = Client(account_sid, auth_token)


def send_message(to: str, message: str):
    
    if message.lower().__contains__("hi") | message.lower().__contains__("hello") :
            conversation = client.conversations.conversations.create(friendly_name=to.split('+')[1])

        #  conversation.messages.create(
        #     author="Bot",
        #     from_='whatsapp:+263781145836',
        #     body="Hi there! Please enter your first name and surname ",
        #     to=to
        # )
            client.conversations.conversations(conversation.sid).messages.create(
                from_='whatsapp:+263781145836',
                body="Hi there! Please enter your first name and surname ",
            )
        
        
    #  conversation.messages.create(author='me', body='Hello, world!')

                     
       
    if message.__contains__("mbuya"):
           messsage = client.messages.create(
            from_='whatsapp:+263781145836',
            body='bhooo',
            to=to
        )
           print("Message",message)
     
def get_message():
    print(client)
    conversations = client.messages.list(to='whatsapp:+263778939867',from_='whatsapp:+263781145836')
    # for conversation in conversations:
        # print(conversation['sid'])
    # messages = client.conversations \
    #              .v1 \
    #              .conversations('ACb467aa16c4499bf8d0866105b07417dd') \
    #              .messages \
    #              .list(limit=20)

    return conversations

  
