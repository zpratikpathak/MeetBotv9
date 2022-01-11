from chromium_Scripts import browser
from automate import updater
from telegram import ChatAction


import os
from dotenv import load_dotenv

load_dotenv()
USER_ID = os.getenv("USER_ID")


def meet_url(context, url_meet):
    browser.get(url_meet)
    context.bot.send_message(chat_id=USER_ID, text="Joined the meet")


def meet(update, context):
    user = update.message.from_user
    if user["id"] == int(USER_ID):
        context.bot.send_chat_action(chat_id=USER_ID, action=ChatAction.TYPING)
        url_meet = update.message.text.split()[-1]
        if len(url_meet) == 12:
            url_meet = "https://meet.google.com/{}".format(url_meet)
            meet_url(context, url_meet)
        elif len(url_meet) == 10:
            url_meet = url_meet[:3] + "-" + url_meet[3:5] + "-" + url_meet[5:]
            url_meet = "https://meet.google.com/{}".format(url_meet)
            meet_url(context, url_meet)
        elif len(url_meet) > 5:
            meet_url(context, url_meet)
        else:
            context.bot.send_message(
                chat_id=USER_ID, text="Oops! You forget to pass the google meet url"
            )
            context.bot.send_message(
                chat_id=USER_ID, text="Use /meet command like this 👇"
            )
            context.bot.send_message(
                chat_id=USER_ID, text="/meet https://meet.google.com/meet-code-value"
            )
    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )
