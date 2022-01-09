from telegram.ext import Updater
from telegram.ext import CommandHandler, Job, Filters, MessageHandler
from telegram import ChatAction

import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

updater = Updater(token=BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# autowrite userid in .env file
def start(update, context):
    user = update.message.from_user
    # print(user)
    context.bot.send_chat_action(chat_id=user['id'], action=ChatAction.TYPING)
    update.message.reply_text('Hello {}!'.format(user['first_name']))
    update.message.reply_text('Your UserID is: {} '.format(user['id']))

def echo(update, context):
    update.message.reply_text(
        "This is not a valid command\nUse /help to list out the available commands"
    )

def help(update, context):
    user = update.message.from_user
    if user['id'] == int(USER_ID):
        context.bot.send_message(
            chat_id=USER_ID,
            text="/mlogin - To login your account\n/meet - To join a meet (Use Example: '/meet https://meet.google.com/mee-tco-deval')\n/status - To get current Screenshot of Joined meet\n/exit - To leave a meeting\n/reset - To reset chromium browser (in Development)\n/owner-To know about me\n/help - To Display this message",
        )
    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )

def owner(update, context):
    update.message.reply_text("My code lies around the whole Internet 😇\nIt was assembled, modified and upgraded by Pathak Pratik\nSource Code is available here👇\nhttps://github.com/zpratikpathak/\n/userid - Your Userid",)

def main():
    dp.add_handler(CommandHandler("start", start, run_async=True))
    dp.add_handler(CommandHandler("help", help, run_async=True))
    dp.add_handler(CommandHandler("owner", owner, run_async=True))
    dp.add_handler(MessageHandler(Filters.text, echo, run_async=True))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()