#!/usr/bin/python
## shed.py
## - ptyhon slack history export daily
## version 0.0.3 - working
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
        for channel in cli.channels:
            slack.user_channel_history(cli.start_date,channel,user)

#-------------------------------------------------
def main():
    cli.try_handle_args()
    slack.initialize()
    shed()

#-------------------------------------------------
if __name__ == "__main__":
    main()

##################################################
