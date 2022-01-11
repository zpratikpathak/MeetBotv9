from telegram.ext import Updater
from telegram.ext import CommandHandler, Filters, MessageHandler
from telegram import ChatAction

from chromium_Scripts import browser, telegram_bot_sendtext

from os import execl
from sys import executable

import os
from dotenv import load_dotenv

load_dotenv()

import pickle

import shutil

from gscripts.login import login
from gscripts.meet import meet


BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")

updater = Updater(token=BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# Feature addition autowrite userid in .env file
def start(update, context):
    user = update.message.from_user
    # print(user)
    context.bot.send_chat_action(chat_id=user["id"], action=ChatAction.TYPING)
    update.message.reply_text("Hello {}!".format(user["first_name"]))
    update.message.reply_text("Your UserID is: {} ".format(user["id"]))

    # Removed ChromeDriver Dependency
    # if chromedriverCheck():
    #     from chromium_Scripts import str1

    #     update.message.reply_text(
    #         "please download correct chromedriver version :", str1[0:2]
    #     )
    #     update.message.reply_text(
    #         "Download it from here :", "https://chromedriver.chromium.org/downloads"
    #     )


def echo(update, context):
    update.message.reply_text(
        "This is not a valid command\nUse /help to list out the available commands"
    )


def help(update, context):
    user = update.message.from_user
    if user["id"] == int(USER_ID):
        context.bot.send_message(
            chat_id=USER_ID,
            text="/login - Login in Google Meet\n/meet - Join a meet\n/status - Screenshot of Joined meet\n/restart - To leave a meeting\n/reset - Reset chrome browser (in Development)\n/owner-To know about me\n/help - To Display this message",
        )
    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )


def owner(update, context):
    update.message.reply_text(
        "My code lies around the whole Internet 😇\nIt was assembled, modified and upgraded by Pathak Pratik\nSource Code is available here👇\nhttps://github.com/zpratikpathak/",
    )


# To do, send a message to the user when the bot is restarted : Finished
def restart(update, context):
    user = update.message.from_user
    if user["id"] == int(USER_ID):
        context.bot.send_message(chat_id=USER_ID, text="Restarting, Please wait!")
        pickle.dump("restart msg check", open("restart.pkl", "wb"))
        browser.quit()
        execl(executable, executable, "automate.py")
    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )


def status(update, context):
    user = update.message.from_user
    if user["id"] == int(USER_ID):
        browser.save_screenshot("snapshot.png")
        context.bot.send_chat_action(chat_id=USER_ID, action=ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(
            chat_id=USER_ID, photo=open("snapshot.png", "rb"), timeout=100
        )
        os.remove("snapshot.png")
    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )


def reset(update, context):
    user = update.message.from_user
    if user["id"] == int(USER_ID):
        if os.path.exists("ChromiumData") or os.path.exists("gmeet.pkl"):

            try:
                browser.quit()
                shutil.rmtree("ChromiumData")
                try:
                    os.remove("gmeet.pkl")
                except:
                    pass
                context.bot.send_message(
                    chat_id=USER_ID, text="Chrome Reset Succesfull"
                )
                execl(executable, executable, "automate.py")
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        else:
            context.bot.send_message(
                chat_id=USER_ID, text="Browser is already clear..."
            )
    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )


def main():

    if os.path.exists("restart.pkl"):
        try:
            os.remove("restart.pkl")
            telegram_bot_sendtext("Bot Restarted")
        except:
            pass

    dp.add_handler(CommandHandler("start", start, run_async=True))
    dp.add_handler(CommandHandler("help", help, run_async=True))
    dp.add_handler(CommandHandler("owner", owner, run_async=True))
    dp.add_handler(CommandHandler("restart", restart, run_async=True))
    dp.add_handler(CommandHandler("status", status, run_async=True))
    dp.add_handler(CommandHandler("reset", reset, run_async=True))
    dp.add_handler(CommandHandler("login", login, run_async=True))
    dp.add_handler(CommandHandler("meet", meet, run_async=True))
    dp.add_handler(MessageHandler(Filters.text, echo, run_async=True))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

# To Do: Add restart feature : Finished
