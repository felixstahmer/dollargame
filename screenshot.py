from selenium import webdriver 
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

def take_screenshot(url):
    chromedriver = "/usr/local/bin/chromedriver"
    browser = webdriver.Chrome(chromedriver)

    browser.get(url)

    time.sleep(10)  # wait 10 seconds for the site to load.

    button = browser.find_element(By.CLASS_NAME, 'Hint_SkipBtn__2HsyR')
    if button:
        button.click()
    

    time.sleep(5)

    dst_url = "img/screenshot.png"
    browser.save_screenshot(dst_url)

    return dst_url