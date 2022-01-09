from selenium import webdriver
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_ID = os.getenv("USER_ID")
import pathlib

scriptDirectory = pathlib.Path().absolute()


options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=1200,800")
options.add_argument(f"user-data-dir={scriptDirectory}\\ChromiumData")

options.add_experimental_option(
    "prefs",
    {
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
        "profile.default_content_setting_values.notifications": 2,
    },
)


def telegram_bot_sendtext(bot_message):
    send_text = (
        "https://api.telegram.org/bot"
        + BOT_TOKEN
        + "/sendMessage?chat_id="
        + USER_ID
        + "&parse_mode=Markdown&text="
        + bot_message
    )
    requests.get(send_text)


test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

browser = webdriver.Chrome(options=options)
str1 = browser.capabilities["browserVersion"]
str2 = browser.capabilities["chrome"]["chromedriverVersion"].split(" ")[0]

if str1[0:2] != str2[0:2]:
    telegram_bot_sendtext("please download correct chromedriver version :", str1[0:2])
    telegram_bot_sendtext(
        "Download it from here :", "https://chromedriver.chromium.org/downloads"
    )