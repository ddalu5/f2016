# f2016
f2016 is a simple Slack bot that tells people to not TALK about the year 2016.

## How to?

Start by installing the requirements:
`pip install -r requirements.txt`

Then go to https://my.slack.com/services/new/bot and add the bot integration by
setting the username. After you validate, an API token will be displayed so save
it for latter.

Now go to the script bot.py and replace the content of the constant `BOT_NAME` by
the username you choose during the bot integration phase, and replace the
content of the constant `BOT_SLACK_BOT_TOKEN` by the API token you received.

Now go to you Slack chat and add the bot to the channels you want and run the script.
