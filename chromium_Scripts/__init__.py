from selenium import webdriver
import chromedriver_autoinstaller
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
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")


options.add_argument(f"user-data-dir={scriptDirectory}\\ChromiumData")

options.add_argument(
    "user-agent='User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'"
)

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


chromedriver_autoinstaller.install()
browser = webdriver.Chrome(options=options)

""" Added Auto Chrome Driver Installer
str1 = browser.capabilities["browserVersion"]
str2 = browser.capabilities["chrome"]["chromedriverVersion"].split(" ")[0]


def chromedriverCheck():

    if str1[0:2] != str2[0:2]:
        return True
    else:
        return False


if chromedriverCheck():
    telegram_bot_sendtext(
        "Please download correct chromedriver version : {}".format(str1[0:2])
    )
    telegram_bot_sendtext(
        "Download it from here : https://chromedriver.chromium.org/downloads"
    )
"""
