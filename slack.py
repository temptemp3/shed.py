#!/usr/bin/python
# -*- coding: utf8 -*-
## slack.py
## - slack functions
## version 0.0.6 - slack token config
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
#-------------------------------------------------
try:
    import slack_config
    config_slack_token=slack_config.slack_token
except ImportError:
    config_slack_token=''
##################################################
## functions
##################################################
def channel_ids():
    channel_ids=[]
    for channel in channels["channels"]:
        channel_ids.append(
            channel["id"])
    return channel_ids

#-------------------------------------------------
def list_channel_names():
    print "available channels:"
    for channel in channels["channels"]:
	print "-c %s" % channel["name"]

#-------------------------------------------------
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
def user_channel_history(start_date,channels,users):
    for channel in channels:
        for message in channel_history(channel,start_date):
            if 'user' in message and message["user"] in users:
                #user_real_name=get_user_real_name_by_id(
                #    message["user"])
                user_real_name="user"
	        message_ts=message_ts_ftime(
                    message["ts"])
                #---------------------------------
		# message text
                #---------------------------------
                #message_text=message["text"]
                message_text=message_text_final(
                    message["text"])
                #---------------------------------
                # skip messages with blank text
                if message_text == '':
                    continue
                #---------------------------------
                # experimental workaround for unicode encode error
                # - can fix by setting appropriate environment settings
		#try:
		#	print message_text
		#except UnicodeEncodeError:
		#	message_text="%s %s" % ("STRING",len(message_text))
                #---------------------------------
                print "\"%s\",\"%s\",\"%s\",\"%s\"" % (
                    channel_name(channel),
                    user_real_name,
                    message_ts,
                    message_text)

#-------------------------------------------------
def channel_id(channel_key):
    for channel in channels["channels"]:
        if  channel["id"]  == channel_key \
        or  channel["name"] == channel_key:
            return channel["id"]
    return None

#-------------------------------------------------
def channel_name(candidate_channel_id):
    for channel in channels["channels"]:
        if channel["id"]  == candidate_channel_id:
            return channel["name"]
    return None

#-------------------------------------------------
# channels.history
def channel_history(candidate_channel,start_date):

    history=[]

    start_date_ts=(
        calendar.timegm(start_date))

    response = sc.api_call(
        "channels.history",
        channel=candidate_channel, 
        oldest=start_date_ts,
        count=1000)

    if response["ok"] == True :
        history=response["messages"]
    else:
        ## not ok but ok
        ## - better allow for now due to errors
        ##   when testing no args behavior
        ## + may look into later
        #sys.exit(2)
        pass

    return history

#-------------------------------------------------
def user_ids():
    user_ids=[]
    for user in users['members']:
        user_ids.append(
            user['id'])
    return user_ids

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
def get_user_real_name_by_id(candidate_member_id):
    for member in users["members"]:
        if member["id"] == candidate_member_id:
            return member["profile"]["real_name"]
    return None

#-------------------------------------------------
def user_id(user_key):
    for member in users["members"]:
        if  member["id"] == user_key \
        or  member["profile"]["real_name"] == user_key :
            return member["id"]
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

    if not config_slack_token:
        slack_token = os.environ["SLACK_API_TOKEN"]
    else:
        slack_token = config_slack_token

    sc = SlackClient(slack_token)

#-------------------------------------------------
def initialize_globals():
    list_channels()
    #list_channel_names()
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
