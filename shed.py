#!/usr/bin/python
## shed.py
## - ptyhon slack history export daily
## version 0.0.5 - empty channel behavior
##################################################
## imports
##################################################
import cli
import slack
##################################################
## functions
##################################################
def shed():
    for user in cli.users:
        for channel in channels():
            slack.user_channel_history(
                cli.start_date,slack.channel_id(channel),slack.user_id(user))

#-------------------------------------------------
def channels():
    if not cli.channels:
        return slack.channel_ids()
    else:
        return cli.channels

#-------------------------------------------------
def main():
    cli.try_handle_args()
    slack.initialize()
    shed()

#-------------------------------------------------
if __name__ == "__main__":
    main()

##################################################
