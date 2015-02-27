Voicemail Victim
===

A live (and legal) target to simulate a victim of voicemail hacking.

Caller ID spoofing is [legal in the United States](http://www.spoofcard.com/blog/2012/12/14/the-verdict-is-in-appeals-court-rules-non-harmful-caller-id-spoofing-is-legal/) if it is not done with "the intent to defraud, cause harm, or wrongfully obtain anything of value".

Disclamer: This application is meant for educational purposes only.

This web application utilizes Twilio TwiML to connect to a live phone number (provided by you) and Heroku's free tier web hosting to quickly deploy a free instance of this application.  You only need to pay for a Twilio phone number (1-2 dollars per month) and its usage (1-2 cents per minute).

If you want to deploy and tweak your own voicemail victim follow the steps below.  Otherwise feel free to mooch on a [pre-deployed instance](https://voicemail-victim.herokuapp.com/configure) and just point your Twilio number at it by jumping to Step 3 below.

## 1) Register

First, you should [sign up](https://www.twilio.com/try-twilio) for a free Twilio account.  In Twilio you will need to purchase a local or toll-free number.  A local number is more realistic, but toll-free lets you absorb any telephone charges a caller would normally pay by charging you a little extra per call.

You should also [sign up](https://signup.heroku.com/) for a free Heroku account.

## 2) Deploy

In order for Twilio to communicate with your web application, it needs to be deployed on the public Internet.

Click the button below to automatically set up the app using your Heroku account.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

If you prefer to run your application locally, please make sure that you have Python and `pip` installed. Please install the required packages:

    pip install -r requirements.txt

Simply run the application by `python server.py`.  You can tunnel `localhost` to the public Internet using [ngrok](https://ngrok.com/): 

    ngrok 5000

To run the app in debug mode (with a stacktrace and an interactive shell on errors), export or set the environment variable `DEBUG` to `True`.

`export DEBUG=True`

Debug mode is not suitable for production!

## 3) Configure

Navigate to [https://www.twilio.com/user/account/phone-numbers/incoming](https://www.twilio.com/user/account/phone-numbers/incoming).  Select your Twilio phone number you wish to connect to the Voicemail Victim web application.  Under `Voice` enter your Heroku application URL for the `/call` endpoint (e.g. `https://voicemail-victim.herokuapp.com/call`) in the `Request URL` field.  Press `Save` to apply the changes.

## 4) Test

You can test by calling your Twilio phone number that you configured to point at the deployed Voicemail Victim web application instance.

Alternatively you can test by making GET requests to the `/call` endpoint with various `To` and `From` parameter values.

Example: [https://voicemail-victim.herokuapp.com/call?To=15158675309&From=12223334444](https://voicemail-victim.herokuapp.com/call?To=15158675309&From=12223334444).
