from helper.twilio_api import send_message, get_message

# from twilio_api import send_message

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return 'All is well...'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        sender_id = request.form['From']

        # Get response from Openai
        send_message(sender_id, message)
    except:
        pass
    return 'OK', 200

@app.route('/twilio/getmesages', methods=['GET'])
def getMessages():

    return get_message()
    


if __name__ == '__main__':
    app.run(debug=True)