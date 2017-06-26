"""
Routes for bot module. This module will handle bot messages as well as Twilio requests
"""
from . import bot
from slackclient import SlackClient
from twilio import twiml
from twilio.rest import Client
import os
from flask import request, Response, current_app

slack_client = SlackClient(os.environ.get("SLACK_BOT_OAUTH_ACCESS_TOKEN", None))
slack_user = os.environ.get("SLACK_USER")
twilio_client = Client()


@bot.route("/twilio", methods=["POST", "GET"])
def twilio_post():
    """
    Handles Twilio post requests. This post request will come from Twilio
    :return Response from Twilio
    """
    response = twiml.TwiML()
    if request.form['From'] == current_app.config.get("USER_NUMBER"):
        message = request.form['Body']
        slack_client.api_call("im.open", text=message, user=slack_user)
    return Response(response.to_xml(), mimetype="text/xml"), 200


@bot.route("/slack", methods=["POST", "GET"])
def slack_post():
    """
    This will handle post requests from Slack. This post request will come from Slack
    When a message is sent to @butlerbot in a channel a POST request is sent to this app
    and a message is then sent from Twilio to this application
    :return:
    """
    if request.form["token"] == current_app.config.get("SLACK_WEBHOOK_SECRET"):
        channel = request.form["channel_name"]
        username = request.form["user_name"]
        text = request.form["text"]
        response_message = "{} in {} says {}".format(username, channel, text)
        twilio_client.messages.create(to=current_app.config.get("USER_NUMBER"),
                                      from_=current_app.config.get("TWILIO_NUMBER"),
                                      body=response_message)
    return Response(), 200
