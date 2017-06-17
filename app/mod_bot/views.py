from . import bot
from slackclient import SlackClient
from twilio import twiml
from twilio.rest import TwilioHttpClient
import os

slack_client = SlackClient(os.environ.get("BOT_API_TOKEN", None))
twilio_client = TwilioHttpClient()


@bot.route("/twilio", methods=["POST"])
def twilio_post():
    pass
