from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
import os
import twilio.twiml

DEFAULT_PASSWORD = 1234
password = os.environ.get("PASSWORD", DEFAULT_PASSWORD)

DEFAULT_PROVIDER = "Small Biz Telecom"
provider = os.environ.get("PROVIDER", DEFAULT_PROVIDER)

app = Flask(__name__, static_url_path='/static')

@app.route('/call', methods=['GET', 'POST'])
def call():
  response = twilio.twiml.Response()
  response.say("Hello, the number you have called is not availble to take your call.  Please leave a message.")
  return str(response)

@app.route('/configure', methods=['GET', 'POST'])
def configure():
  return render_template('configure.html')

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('index.html')

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
