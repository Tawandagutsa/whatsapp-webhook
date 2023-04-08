import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACb467aa16c4499bf8d0866105b07417dd'
auth_token = 'dd8b1ca2e094f2647de9fabd7c8bae73'
client = Client(account_sid, auth_token)

# conversations = client.messages.list(from_='whatsapp:+263778939867',to='whatsapp:+263781145836')

conversations = client.conversations.conversations.list()
print("Conversation : ", conversations)
for conversation in conversations:
  messages = conversation.messages.list()
  
  for message in messages:
        print("Body:", message.body)


                    
#                 messages=  client.conversations.messages(conversation.sid)
# print("this is a message",messages.)      
# for record in messages:
#     print(record.sid)
                 
# for record in conversations:
#     print(record)