import os
from flask import Flask, request
from twilio.util import TwilioCapability
import twilio.twiml

DEFAULT_PASSWORD = 1234

app = Flask(__name__)
password = os.environ.get("PASSWORD", DEFAULT_PASSWORD)

@app.route('/call', methods=['GET', 'POST'])
def call():
  response = twilio.twiml.Response()
  response.say("Hello, the number you have called is not availble to take your call.  Please leave a message.")
  return str(response)

@app.route('/', methods=['GET', 'POST'])
def welcome():
  response = twilio.twiml.Response()
  response.say("Voicemail Victim is live!")
  return str(response)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)