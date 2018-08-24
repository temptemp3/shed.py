#!/usr/bin/python
## shed.py
## - ptyhon slack history export daily
## version 0.0.6 - no args behavior
##################################################
## imports
##################################################
from datetime import date
#-------------------------------------------------
import cli
import slack
##################################################
## functions
##################################################
def shed():
    ## debug
    #print "start date: %s" % start_date
    #print "users: %s" % users
    #print "channels: %s" % channels
    #return
    slack.user_channel_history(
        start_date,
        channels,
        users)

#-------------------------------------------------
def start_date():
    if not cli.start_date:
        return date.today().timetuple()
    else:
        return cli.start_date

#-------------------------------------------------
def channels():
    if not cli.channels:
        return slack.channel_ids()
    else:
        return map(slack.channel_id,cli.channels)
        return cli.channels

#-------------------------------------------------
def users():
    if not cli.users:
        return slack.user_ids()
    else:
        return list(filter(lambda u: u is not None,
            list(map(lambda u:slack.user_id(u),cli.users))))

#-------------------------------------------------
def initialize_globals():
    global start_date
    global channels
    global users
    start_date=start_date()
    channels=channels()
    users=users()

#-------------------------------------------------
def main():
    cli.try_handle_args()
    slack.initialize()
    initialize_globals()
    shed()

#-------------------------------------------------
if __name__ == "__main__":
    main()

##################################################
