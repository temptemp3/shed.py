#!/usr/bin/python
## shed.py
## - ptyhon slack history export daily
## version 0.0.2 - export cli, import slack
##################################################
## imports
##################################################
from datetime import datetime
#-------------------------------------------------
import cli
import slack
##################################################
## functions
##################################################
def shed():
    ## debug
    #print cli.start_date
    #print cli.user
    #print cli.channels
    #return
    ## debug
    #print "start_date: %s" % start_date
    #print "user: %s" % user
    #print "channels: %s" % channels
    print "%s,%s,%s,%s" % (channels[0], user,datetime(start_date.year,start_date.month,start_date.day),"MESSAGE")
#-------------------------------------------------
def main():
    #---------------------------------------------
    cli.try_handle_args()
    global start_date
    global user
    global channels
    start_date=cli.start_date
    user=cli.user
    channels=cli.channels
    return
    #---------------------------------------------
    slack.initialize()
    ## debug
    #print slack.channels
    #print slack.history
    #print slack.users
    #print slack.info
    #---------------------------------------------
    shed()
    #---------------------------------------------

#-------------------------------------------------
if __name__ == "__main__":
    main()
##################################################
