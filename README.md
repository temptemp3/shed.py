# shed.py

[shed.sh](https://github.com/temptemp3/shed.sh) in python

## requirements and installation

**requirements and instalation**

requires [python-slackclient](python-slackclient)

```
pip install slackclient
```

see [python-slackclient requirements and installation](https://github.com/slackapi/python-slackclient#requirements-and-installation)

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
