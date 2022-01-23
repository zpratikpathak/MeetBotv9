from chromium_Scripts import browser
from telegram import ChatAction
import os
import pickle
import time

from dotenv import load_dotenv

load_dotenv()
USER_ID = os.getenv("USER_ID")
GMAIL_USERNAME = os.getenv("GMAIL_USERNAME")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")


def login(update, context):
    user = update.message.from_user
    if user["id"] == int(USER_ID):
        if os.path.exists("gmeet.pkl"):
            context.bot.send_message(
                chat_id=USER_ID,
                text="Already Logged In! Run /meet meeting_url to join meeting",
            )
            context.bot.send_message(
                chat_id=USER_ID,
                text="Still getting some error? try using /reset",
            )
            return
        try:
            '''
            context.bot.send_chat_action(chat_id=user["id"], action=ChatAction.TYPING)
            update.message.reply_text("Logging in...")
            browser.get(
                "https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow"
            )
            time.sleep(2)
            browser.find_element_by_id("identifierId").send_keys(GMAIL_USERNAME)
            time.sleep(7)
            browser.find_element_by_id("identifierNext").click()
            time.sleep(2)
            browser.find_element_by_name("password").send_keys(GMAIL_PASSWORD)
            time.sleep(7)
            browser.find_element_by_id("passwordNext").click()
            time.sleep(2)
            update.message.reply_text("Logged in!")
            browser.get("https://meet.google.com/")
            browser.save_screenshot("snapshot.png")
            context.bot.send_chat_action(
                chat_id=USER_ID, action=ChatAction.UPLOAD_PHOTO
            )
            context.bot.send_photo(
                chat_id=USER_ID, photo=open("snapshot.png", "rb"), timeout=100
            )

            os.remove("snapshot.png")
            '''

            browser.get(
                "https://accounts.google.com/o/oauth2/auth/identifier?client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&scope=profile%20email&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3Abbc%2C16%3Afad07e7074c3d678%2C10%3A1601127482%2C16%3A9619c3b16b4c5287%2Ca234368b2cab7ca310430ff80f5dd20b5a6a99a5b85681ce91ca34820cea05c6%22%2C%22cdl%22%3Anull%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%22d18871cbc2a3450c8c4114690c129bde%22%7D&response_type=code&flowName=GeneralOAuthFlow"
            )
            username = browser.find_element_by_id("identifierId")
            username.send_keys(GMAIL_USERNAME)
            nextButton = browser.find_element_by_id("identifierNext")
            nextButton.click()
            time.sleep(7)

            browser.save_screenshot("ss.png")
            context.bot.send_chat_action(
                chat_id=USER_ID, action=ChatAction.UPLOAD_PHOTO)
            mid = context.bot.send_photo(
                chat_id=USER_ID, photo=open("ss.png", "rb"), timeout=120
            ).message_id
            os.remove("ss.png")

            password = browser.find_element_by_xpath(
                "//input[@class='whsOnd zHQkBf']")
            password.send_keys(GMAIL_PASSWORD)
            signInButton = browser.find_element_by_id("passwordNext")
            signInButton.click()
            time.sleep(7)

            if browser.find_elements_by_xpath('//*[@id="authzenNext"]/div/button/div[2]'):
                context.bot.send_chat_action(
                    chat_id=USER_ID, action=ChatAction.TYPING)
                context.bot.send_message(
                    chat_id=USER_ID, text="Need Verification. Please Verify"
                )
                browser.find_element_by_xpath(
                    '//*[@id="authzenNext"]/div/button/div[2]'
                ).click()
                time.sleep(5)

                browser.save_screenshot("ss.png")
                context.bot.send_chat_action(
                    chat_id=USER_ID, action=ChatAction.UPLOAD_PHOTO)
                mid = context.bot.send_photo(
                    chat_id=USER_ID, photo=open("ss.png", "rb"), timeout=120
                ).message_id
                os.remove("ss.png")
                time.sleep(20)

            browser.get("https://meet.google.com")
            time.sleep(7)

            pickle.dump("Meet Login: True", open("gmeet.pkl", "wb"))

        except:
            update.message.reply_text("Auto login failed!")
            browser.get(
                "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmeet.google.com%2F&service=cl&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
            )
            update.message.reply_text("We have opened login page for you")
            update.message.reply_text("Please login manually")
            update.message.reply_text("Don't worry, it's a one time procedure")

            c = 0
            while True:
                try:
                    if browser.find_elements_by_xpath('//*[@id="gb"]/'):
                        update.message.reply_text("Login Successful")
                        break
                except:
                    pass
                time.sleep(1)
                c += 1
                if c == 300:
                    update.message.reply_text("Login Failed")
                    pickle.dump("Meet Login: True", open("gmeet.pkl", "wb"))
                    break

    else:
        update.message.reply_text(
            "You are not authorized to use this bot.\nUse /owner to know about me"
        )
    # context.bot.send_chat_action(chat_id=USER_ID, action=ChatAction.TYPING)
