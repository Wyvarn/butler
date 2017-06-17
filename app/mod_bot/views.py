from . import bot
from slackclient import SlackClient
from twilio import twiml
from twilio.rest import Client
import os
from flask import request, Response, current_app

slack_client = SlackClient(os.environ.get("BOT_API_TOKEN", None))
twilio_client = Client()


@bot.route("/twilio", methods=["POST"])
def twilio_post():
    """
    Handles Twilio post requests. This post request will come from Twilio
    """
    response = twiml.TwiML()
    if request.form['From'] == current_app.config.get("USER_NUMBER"):
        message = request.form['Body']
        slack_client.api_call("chat.postMessage", channel="#general",
                              text=message, username='butlerbot', icon_emoji=':robot_face:')
    return Response(response.to_xml(), mimetype="text/xml"), 200
