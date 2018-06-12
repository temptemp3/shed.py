#!/usr/bin/python
## shed.py
## - ptyhon slack history export daily
## version 0.0.1 - initial
##################################################
## imports
##################################################
import getopt, sys
#---
from datetime import date
from datetime import datetime
#---
from string import split
##################################################
## functions
##################################################
def shed():
    print "start_date: %s" % start_date
    print "user: %s" % user
    print "channels: %s" % channels
    print "%s,%s,%s,%s" % (channels[0], user,datetime(start_date.year,start_date.month,start_date.day),"MESSAGE")
#-------------------------------------------------
def on_date(candidate_date):
    global start_date
    start_date=date.today()
    date_yy_mm_dd=split(candidate_date,"-",3)
    if len(date_yy_mm_dd) == 3:
        year=date_yy_mm_dd[0]
        month=date_yy_mm_dd[1]
        day=date_yy_mm_dd[2]
        try:
            start_date=date(
                    int(year),int(month),int(day))
        except ValueError as err:
            print str(err)
            sys.exit(3)
#-------------------------------------------------
# to do:
# + only accept first user provided
def on_user(candidate_user):
    global user
    user=candidate_user
#-------------------------------------------------
channels=[]
def on_channel(candidate_channel):
    global channels
    channels.append(candidate_channel)
#-------------------------------------------------
def handle_args():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d:u:c:", [])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        #usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o in ("-d"):
	    on_date(a)
            #print start_date
    	elif o in ("-u"):
	    on_user(a)
            #print user
    	elif o in ("-c"):
	    on_channel(a)
            #print channels
        else:
            assert False, "unhandled option"
#-------------------------------------------------
def main():
    handle_args()
    shed()
#-------------------------------------------------
if __name__ == "__main__":
    main()
##################################################
