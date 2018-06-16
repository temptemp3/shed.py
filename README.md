# shed.py

[shed.sh](https://github.com/temptemp3/shed.sh) in python

## requirements and installation

**requirements**

 + [python-slackclient](python-slackclient)
 
**instalation**

 1. [install python-slackclient](https://github.com/slackapi/python-slackclient#requirements-and-installation)


**environment**

```
alias shed='python /path/to/shed.py'
SLACK_API_TOKEN='your-slack-api-token'
```

**usage**

```
shed -dcu

-d - start date (default: date today)
-c - channel name or id (default: all channels)
-u - user name or id (default all uesrs)
```
