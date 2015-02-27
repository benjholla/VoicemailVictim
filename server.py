from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
import os
import re
import twilio.twiml

DEFAULT_PASSCODE = None
passcode = os.environ.get("PASSCODE", DEFAULT_PASSCODE)

DEFAULT_PROVIDER = "Small Biz Telecom"
provider = os.environ.get("PROVIDER", DEFAULT_PROVIDER)

app = Flask(__name__, static_url_path="/static")

def normalize(phone):
  chars_to_remove = ['(', ')', '-', ' ']
  regex = '[' + re.escape(''.join(chars_to_remove)) + ']'
  return re.sub(regex, '', phone)

@app.route("/call", methods=["GET", "POST"])
def call():
  response = twilio.twiml.Response()
  caller = normalize(request.values.get("From"))
  callee = normalize(request.values.get("To"))
  if caller and callee and (caller == callee):
    if passcode:
      response.say("You have one unheard message.  Please enter your four digit passcode.")
#      TODO: if passcode wrong...
#      response.say("Incorrect passcode.  Reminder. You have not changed your default " + provider + " voicemail passcode.")
    else:
      response.say("You have one unheard message.  First unheard message.")
#     TODO: play message...
  else:
    response.say("Hello, the number you have called is not available to take your call.  Please leave a message.")
#    TODO: record message...
  return str(response)

@app.route("/configure", methods=["GET", "POST"])
def configure():
  return render_template("configure.html")

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html")

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port, debug=True)
