#!/usr/bin/python
## slack.py
## - slack functions
## version 0.0.2 - working
##################################################
#
#    METHODS
#    - channels.list
#    - channels.history
#    - users.list
#    - users.info
#
##################################################
## imports
##################################################
import os
import json
import re
from string import replace
from datetime import datetime
import calendar
from calendar import timegm
#-------------------------------------------------
from slackclient import SlackClient
##################################################
## functions
##################################################
# channels.list
def list_channels(): 

    global channels

    response = sc.api_call(
        "channels.list"
    )

    if response["ok"] == True :
        channels=response
    else :
        sys.exit(1)

#-------------------------------------------------
def message_ts_ftime(candidate_message_ts):
    return datetime.fromtimestamp(
	float(candidate_message_ts)).strftime("%m/%d/%y %H:%M")

#-------------------------------------------------
def message_text_final(candidate_message_text):
    users=re.findall("<@U[^>]*.",candidate_message_text)
    if users:
        for user in users:
            member_id=(replace(replace(
                user,"<@",""),">",""))
	    return replace(candidate_message_text,
                    user,get_user_real_name_by_id(member_id))
    return candidate_message_text

#-------------------------------------------------
def user_channel_history(start_date,candidate_channel,candidate_user):
    user_real_name=get_user_real_name_by_id(candidate_user)
    channel=channel_name(candidate_channel)
    channel_history(candidate_channel,start_date)
    for message in history["messages"]:
        if 'user' in message and message["user"] == candidate_user:
	    message_ts=message_ts_ftime(message["ts"])
            message_text=message_text_final(message["text"])
            print "\"%s\",\"%s\",\"%s\",\"%s\"" % (
                channel,user_real_name,message_ts,message_text)

#-------------------------------------------------
def channel_name(candidate_channel_id):
    for channel in channels["channels"]:
        if channel["id"]  == candidate_channel_id:
            return channel["name"]
    return None

#-------------------------------------------------
# channels.history
def channel_history(candidate_channel,start_date):

    global history

    start_date_ts=(
        calendar.timegm(start_date))

    response = sc.api_call(
        "channels.history",
        channel=candidate_channel, 
        oldest=start_date_ts,
        count=1000
    )

    if response["ok"] == True :
        history=response
    else :
        sys.exit(2)

#-------------------------------------------------
# users.list
def list_users():

    global users
    
    response = sc.api_call(
        "users.list"
    )

    if response["ok"] == True :
        users=response
    else :
        sys.exit(3)
        
#-------------------------------------------------
def first_user_id():
    return users["members"][0]["id"]

#-------------------------------------------------
def get_user_real_name_by_id(candidate_member_id):
    for member in users["members"]:
        if member["id"] == candidate_member_id:
            return member["profile"]["real_name"]
    return None

#-------------------------------------------------
def user_real_name():
    return info['user']['real_name']

#-------------------------------------------------
# users.info
def user_info(candidate_user):

    global info
    
    response = sc.api_call(
        "users.info",
        user=candidate_user
    )

    if response["ok"] == True :
        info=response
    else :
        sys.exit(4)

#-------------------------------------------------
def payload():

    print 'done'

#-------------------------------------------------
def initialize_client():

    global sc

    slack_token = os.environ["SLACK_API_TOKEN"]

    sc = SlackClient(slack_token)

#-------------------------------------------------
def initialize_globals():
    list_channels()
    list_users()

#-------------------------------------------------
def initialize():
    initialize_client()
    initialize_globals()

#-------------------------------------------------
def main():
    initialize()
    payload()

#-------------------------------------------------
if __name__ == "__main__":
    main()

##################################################
