#!/usr/bin/python
# coding=UTF-8

import re
import time
from slackclient import SlackClient


BOT_NAME = '[PUT BOT USERNAME HERE]'
SLACK_BOT_TOKEN = '[PUT API TOKEN HERE]'
READ_WEBSOCKET_DELAY = 0.3

try:
    from dev import *
except:
    pass


def no_2016(channel):
    wdbit = (
        "(ʘ言ʘ╬)",
        "WE DON'T TALK ABOUT 2016!!!!",
        "(╯°□°）╯︵ ┻━┻",
        "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
        "NEVER TALK ABOUT 2016!!!!"
    )

    for message in wdbit:
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=message, as_user=True)


def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output \
                    and 'user_profile' not in output \
                    and output["text"].strip() != '' \
                    and re.match(r'\D*\s*2016\s*\D*',
                                 output["text"].strip().strip('\u')):
                return output['channel']
    return None

slack_client = SlackClient(SLACK_BOT_TOKEN)


if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                bot_id = user.get('id')
        if bot_id:
            if slack_client.rtm_connect():
                print("StarterBot connected and running!")
                while True:
                    channel = parse_slack_output(slack_client.rtm_read())
                    if channel:
                        no_2016(channel)
                    time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("No user " + BOT_NAME)
