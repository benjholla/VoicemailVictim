Voicemail Victim
===

A live (and legal) target to simulate a victim of voicemail hacking.

Utilizes Twilio TwiML to connect to a live phone number (provided by you) and Heroku's free tier webapp hosting to quickly deploy a free instance of this application.  You are required to enter and pay for the Twilio phone usage.

## 1) Register

Please [sign up](https://www.twilio.com/try-twilio) for a free Twilio account.  In Twilio you will need to purchase a local or toll-free number.  A local number is more realistic, but toll-free lets you absorb any telephone charges a caller would normally pay by charging you a little extra per call.

You should also [sign up](https://signup.heroku.com/) for a free Heroku account.

## 2) Deploy

In order for Twilio to communicate with your web application, it needs to be deployed on the public Internet.

Click the button below to automatically set up the app using your Heroku account.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

If you prefer to run your application locally, please make sure that you have Python and `pip` installed. Please install the required packages:

    pip install -r requirements.txt

Simply run the application by `python server.py`.  You can tunnel `localhost` to the public Internet using [ngrok](https://ngrok.com/): 

    ngrok 5000

## 3) Configure
TODO

## 4) Test
TODO
