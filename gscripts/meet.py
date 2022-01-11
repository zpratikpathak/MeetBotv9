from chromium_Scripts import browser
from automate import updater

import os
from dotenv import load_dotenv

load_dotenv()
USER_ID = os.getenv("USER_ID")


def meet(update, context):

    context.bot.send_chat_action(chat_id=userId, action=ChatAction.TYPING)
    url_meet = update.message.text.split()[-1]
    if len(url_meet) > 5:
        joinMeet(context, url_meet)
    else:
        context.bot.send_message(
            chat_id=userId, text="Oops! You forget to pass the google meet url"
        )
        context.bot.send_message(chat_id=userId, text="Use /meet command like this 👇")
        context.bot.send_message(
            chat_id=userId, text="/meet https://meet.google.com/meet-code-value"
        )
