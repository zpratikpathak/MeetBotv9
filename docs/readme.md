## Requirements
- Python 3.8.x
- Chrome Browser
- Telegram Bot Token ([Get your Token from here](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token "click here"))

## Features
- Join Google Meet
- Leave Google meet
- Auto Google Login
- Clear Browser Data
- Take Screenshot
- Auto Upgradable
- No Driver Dependecies


## Installation
Install Dependecies using command 👇

`pip install -r requirements.txt`

Create a `.env` file in the root directory and add the following credentials

```
BOT_TOKEN = 
USER_ID = 
GMAIL_USERNAME = 
GMAIL_PASSWORD = 
```

- Add BOT_TOKEN 
- Add USER_ID (Bot will send you your "USERID" in first startup, copy it and paste it here)
- Add gmail Username (i.e. Email)
- Add gmail Password

### Note:
+ Disable 2 step authentication
+ If automatic login failed then login manually

## How to run?
Use command

```python automate.py```

## HEADLESS/GUI
You can turn ON/OFF Headless/GUI mode of chrome by commenting/uncommenting `line 18` of `chromium_Scripts/__init__.py`

## How to Stop?
Just close the script.

## TO DO
- Add various deployment Compatability
