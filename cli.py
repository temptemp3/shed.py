#!/usr/bin/python
## cli.py
## - cli for python slack history export daily
## version 0.0.1 - initial
##################################################
## imports
##################################################
import getopt, sys
from datetime import date
from string import split
##################################################
## functions
##################################################
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
def test_args():
    # conditions:
    # 1. have start_date and user
    # 1. channels is not empty
    if 'start_date' not in globals():
        print 'start date not specified'
        sys.exit(1)
    if 'user' not in globals():
        print 'user not specified'
        sys.exit(1)
    if 'channels' not in globals() or len(channels) <= 0 :
        print 'channels not specified'
        sys.exit(1)

#-------------------------------------------------
def try_handle_args():
    handle_args()
    test_args()

#-------------------------------------------------
def main():
    try_handle_args()

#-------------------------------------------------
if __name__ == "__main__":
    main()
##################################################
