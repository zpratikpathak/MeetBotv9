from selenium import webdriver

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

browser = webdriver.Chrome(options=options)


