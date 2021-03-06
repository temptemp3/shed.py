#!/usr/bin/python
## cli.py
## - cli for python slack history export daily
## version 0.0.4 - no args behavior
##################################################
## imports
##################################################
import getopt
import sys
from time import strptime
##################################################
## functions
##################################################
start_date=""
def on_date(candidate_date):

    global start_date
    
    try:
        start_date=strptime(candidate_date, "%Y-%m-%d")
    except ValueError as err:
        print "malformed start date"
        print "format:"
        print " YYYY-MM-DD"
        print "example:"
        print " 2018-06-16"
        sys.exit(3)

#-------------------------------------------------
users=[]
def on_user(candidate_user):
    global user
    users.append(candidate_user)

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
        ## no args behavior
        # print help information and exit:
        #print str(err)  # will print something like "option -a not recognized"
        #usage()
        #sys.exit(2)
        return
    output = None
    verbose = False
    for o, a in opts:
        if o in ("-d"):
	    on_date(a)
            ## debug
            #print start_date
    	elif o in ("-u"):
	    on_user(a)
            ## debug
            #print users
    	elif o in ("-c"):
	    on_channel(a)
            ## debug
            #print channels
        else:
            assert False, "unhandled option"

#-------------------------------------------------
def test_args():
    # conditions:
    # 1. have start_date and user
    # 1. channels is not empty
    ## empyt start_date behavior
    #if 'start_date' not in globals():
    #    print 'start date not specified'
    #    sys.exit(1)
    ## empty user behavior
    #if 'users' not in globals() or len(users) <= 0 :
    #    print 'user not specified'
    #    sys.exit(1)
    ## empy channel behavior
    #if 'channels' not in globals() or len(channels) <= 0 :
    #    print 'channels not specified'
    #    sys.exit(1)
    pass

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
