from flask import Flask
from flask import request
from flask import render_template
import os
import re
import twilio.twiml

# DEFAULT_PASSCODE = str(1234)
DEFAULT_PASSCODE = None
passcode = os.environ.get("PASSCODE", DEFAULT_PASSCODE)

DEFAULT_PROVIDER = "Small Biz Telecom"
provider = os.environ.get("PROVIDER", DEFAULT_PROVIDER)

app = Flask(__name__, static_url_path="/static")

# strips out (, ), -, and space characters
def normalize_phone(phone):
  if phone:
    chars_to_remove = ["(", ")", "-", " "]
    regex = "[" + re.escape("".join(chars_to_remove)) + "]"
    return re.sub(regex, "", phone)
  else:
    return None

# formats the number as x-xxx-xxx-xxxx
def format_phone(phone):                                                                                                                                  
  if phone:
    phone = normalize_phone(phone)
    return format(int(phone[:-1]), ",").replace(",", "-") + phone[-1]
  else:
    return None

# formats the number as x x x x x x x x x x x with spaces for text-to-speech
def say_phone(phone):                                                                                                                                  
  if phone:
    phone = normalize_phone(phone)
    return ' '.join(phone[i:i+1] for i in xrange(0,len(phone),1))
  else:
    return None

# prompts for voicemail passcode and checks it
# plays an obvious hint that the voicemail inbox is still using the default passcode...
def login(response, inbox, passcode, passcode_entered):
  # if this voicemail has a passcode
  if passcode:
    # ask for passcode
    if not passcode_entered:
      response.say("You have reached the voicemail inbox of " + say_phone(inbox) + ".")
      with response.gather(numDigits=4, action="/authenticate", method="POST") as g:
        g.say("Please enter your four digit voicemail passcode to continue.")
    # check passcode
    elif passcode_entered == passcode:
      # correct passcode, play message
      play_message(response)
    else:
      # wrong passcode, give hint and hang up
      response.say("Incorrect passcode.  Reminder. You have not changed your default " + provider + " voicemail passcode.  Goodbye.")
  else:
    response.say("You have reached the voicemail inbox of " + say_phone(inbox) + ".")
    play_message(response)

# plays a silly hardcoded message
# if one was fancy they could add a database and play recorded messages here
# that were saved from the /leave-message endpoint
def play_message(response):
  response.say("You have one unheard message.  First unheard message.")
  response.play("http://demo.twilio.com/hellomonkey/monkey.mp3")
  response.say("You have no unheard messages.  Goodbye.")

@app.route("/call", methods=["GET", "POST"])
def call():
  caller = normalize_phone(request.values.get("From"))
  callee = normalize_phone(request.values.get("To"))
  response = twilio.twiml.messaging_response.MessagingResponse()
  # if the caller is calling himself
  if caller and callee and (caller == callee):
    # login to voicemail
    login(response, callee, passcode, None)
  else:
    # caller is not calling himself, prompt for a message
    response = twilio.twiml.messaging_response.MessagingResponse()
    response.say("Hello, the number you have called is not available to take your call.  Please leave a message after the tone.")
    response.record(maxLength="30", action="/leave-message")
  return str(response)

@app.route("/authenticate", methods=["GET", "POST"])
def authenticate():
  passcode_entered = request.values.get('Digits', None)
  callee = normalize_phone(request.values.get("To"))
  response = twilio.twiml.messaging_response.MessagingResponse()
  login(response, callee, passcode, passcode_entered)
  return str(response)

@app.route("/leave-message", methods=["GET", "POST"])
def leave_message():
  recording_url = request.values.get("RecordingUrl", None)
  response = twilio.twiml.messaging_response.MessagingResponse()
  response.say("Thanks for leaving a message... if you would like to listen to the message you just left, please stay on the line.")
  response.play(recording_url)
  response.say("Goodbye.")
  return str(response)

@app.route("/configure", methods=["GET", "POST"])
def configure():
  return render_template("configure.html")

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html")

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port, debug=os.environ.get("DEBUG", False))
