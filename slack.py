#!/usr/bin/python
## slack.py
## - slack functions
## version 0.0.1 - initial
##################################################
## imports
##################################################
import os
from slackclient import SlackClient
import json
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
        #print response.keys()
        #print response["ok"]
        #print response["headers"]
        #print response["channels"]
        channels=response
    else :
        sys.exit(1)

#-------------------------------------------------
def first_channel_id():
    return channels["channels"][0]["id"]

#-------------------------------------------------
# channels.history
def channel_history(candidate_channel):

    global history

    response = sc.api_call(
        "channels.history",
        channel=candidate_channel
    )

    if response["ok"] == True :
        #print response.keys()
        #print response["has_more"]
        #print response["ok"]
        #print response["messages"]
        #print response["headers"]
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
        #print response.keys()
        #print response["headers"]
        #print response["cache_ts"]
        #print response["ok"]
        #print response["members"]
        users=response
    else :
        sys.exit(3)
        
#-------------------------------------------------
def first_user_id():
    return users["members"][0]["id"]

#-------------------------------------------------
# users.info
def user_info(candidate_user):

    global info
    
    response = sc.api_call(
        "users.info",
        user=candidate_user
    )

    if response["ok"] == True :
        #print response.keys()
        #print response["headers"]
        #print response["ok"]
        #print response["user"]
        info=response
    else :
        sys.exit(4)

#-------------------------------------------------
def payload():

    #---------------------------------------------
    #
    #   METHODS
    #	- channels.list
    #	- channels.history
    #	- users.list
    #	- users.info
    #
    #---------------------------------------------
    #   channels.list
    #print channels
    #   channels.history
    #print history
    #   users.list 
    #print users
    #   users.info
    #print info
    #---------------------------------------------

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
    user_info(first_user_id())
    channel_history(first_channel_id())

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
