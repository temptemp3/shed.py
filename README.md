# shed.py

[shed.sh](https://github.com/temptemp3/shed.sh) in python

**usage**

```
shed -dcu

-d - start date (default: date today)
-c - channel name or id (default: all channels)
-u - user name or id (default all users)
```

**requirements and installation**

requires python-slackclient

```
pip install slackclient
```

see [python-slackclient requirements and installation](https://github.com/slackapi/python-slackclient#requirements-and-installation)

**environment and setting**

(optional) add alias to .bashrc

```
alias shed='python /path/to/shed.py'
```

set slack api token

(option i) use environment

```
SLACK_API_TOKEN='your-slack-api-token'
```

(option ii) use slack_config file

copy [slack_confing_sample](https://github.com/temptemp3/shed.py/blob/master/slack_config_sample.py) to slack_config

set SLACK_API_TOKEN in slack_config
