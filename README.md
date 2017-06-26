# Butler Slack Bot

Slack bot that serves you messages via SMS. This is a simple slack bot that sends you messages to your phone when you receive them on Slack. You can also send slack messages via Text message.

## Requirements

There are a couple of tools you will need to have

1. ***Slack***
    
    This is necessary for accessing Slack messages. And of course you need a slack team or you can create one
    
    + Create an account [here](https://slack.com/) or login in.
    
    + Slack web API docs which can be found [here](https://api.slack.com/web)
        
2. ***Twilio***
    
    Twilio account to enable sms functionality. You can create a free account [here](https://www.twilio.com/try-twilio) and get a free number with SMS capabilities [Check here](https://www.twilio.com/docs/api/rest/sending-messages)
    
3. ***Familiarity with Flask web framework***
    
    This is built on top of flask web framework so familiarity with this framework is required

4. ***Python 2 or 3***
   
   Although this is written in Python 3.6, Python 2.x will still work

5. ***ngrok***
    
    Will make your local host server available globally via a unique address. More information can be found [here](https://ngrok.com/docs)


### Setup

Once you have all the above requirements, you will need the following setup in your environment. 
You can create a `.env` file in the root of your project and add the following:

```plain
FLASK_CONFIG=develop
DATABASE_URL=<YOUR DATABASE URL>
CLIENT_ID=<SLACK CLIENT ID>
CLIENT_SECRET=<SLACK CLIENT SECRET>
VERIFICATION_TOKEN=<SLACK VERIFICATION TOKEN>
SLACK_WEBHOOK_SECRET=<SLACK WEBHOOK SECRET>
SECRET_KEY=<SLACK SECRET KEY>
CSRF_SESSION_KEY=<CSRF SESSION KEY>
BOT_API_TOKEN=<API TOKEN FOR YOUR SLACK BOT>
OAUTH_ACCESS_TOKEN=<OAUTH ACCESS TOKEN FROM SLACK>
TWILIO_ACCOUNT_SID=<TWILIO ACCOUNT SID>
TWILIO_AUTH_TOKEN=<TWILIO AUTH TOKEN>
TWILIO_NUMBER=<TWILIO NUMBER>
USER_NUMBER=<YOUR PHONE NUMBER>
```
> The `<PLACE HOLDERS>` are where you place your keys, api tokens and secrets from both slack and twilio as well as flask configurations. Ensure you have these setup first.

Once that is complete all you are left with is installing requirements and running the application.

Start by serving up ngrok

```bash
./ngrok http 5000
```
> This will forward your subdomoain requests to your localhost subdomain. Ensure that your flask app will serve on port 5000

You should get an output as follows:

![](https://www.twilio.com/blog/wp-content/uploads/2016/05/EbBUKW30VbYxH9riC0RqrIBsDzYwhcsFTeU-MYKne7MT1iXNNChSLDekrjXOw7qwiUN5Lxa_nTu3FXT0W4MQEzJNUBmExphQLn_rzgmsxgCmZR4j2Xh9Y8LwypWCEC3Q7W5_bRn5.png)

The second forwarding address you get (one with https) is what we shall use in configuring the Twilio messaging url. This is the url that messages will be sent to from Twilio

![twilio](https://www.twilio.com/blog/wp-content/uploads/2016/05/XogwzHUT2l6XJHD0jif88nOzegul_41Xw_EtFdXRQTPwKVxGtAZ19c_CGdlaEf_aXV9ImEyF0TWSOfAnIXWyOckZoKR5aax1pDQly8joE5muES7lILCTPsPI8CcGfstD9OBbSu57.png)

Ensure you add a `/bot/twilio` to the end of the url. As this is where Twilio will send incoming messages received on Slack. More detail will be in the code

That should be it. Once you have all these setup. Run the server with:

```bash
$ virtualenv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py runserver
```
> this follows from creating the virtual environment and installing required dependencies, then running the server

You can then proceed to send a message to your Twilio phone number and you should receive a slack message on Slack. The same applies to sending a message on Slack and you should receive a message on you phone number.

References:

1. [https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html](https://www.twilio.com/blog/2016/05/build-sms-slack-bot-python.html) 
   