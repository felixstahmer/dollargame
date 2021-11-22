from selenium import webdriver 
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 

import sys

import time

def take_screenshot(url):
    chromedriver = "/usr/local/bin/chromedriver"
    browser = webdriver.Chrome(chromedriver)

    browser.get(url)

    # browser.execute_script('window.localStorage.setItem("_ym50196268_lsid", "1459009512347");')
    # browser.execute_script('window.localStorage.setItem("game_11",{"Vertices":5,"Genus":0,"Min":-10,"Max":10,"Mode":"Game","GridMode":false,"GridMode1":false,"GridMode2":false,"DelCon":"0_1"});')
    # browser.execute_script('window.localStorage.setItem("lastVisitedLevel__0.0.8", {"worldId":100,"packId":100,"levelId":3});')
    # browser.execute_script('window.localStorage.setItem("userId", "5f7da34d-36b8-4ac9-af13-d391cc8cffba");')

    # browser.add_cookie({'name' : 'game_11', 'value' : '{"Vertices":5,"Genus":0,"Min":-10,"Max":10,"Mode":"Game","GridMode":false,"GridMode1":false,"GridMode2":false,"DelCon":"0_1"}'})
    # browser.add_cookie({'name' : 'userId', 'value' : '5f7da34d-36b8-4ac9-af13-d391cc8cffba'})

    time.sleep(10)  # wait 10 seconds for the site to load.

    try:
        button = browser.find_element(By.CLASS_NAME, 'Hint_SkipBtn__2HsyR')
        button.click()
    except NoSuchElementException:
        print("Button not Found")
        
    
    

    time.sleep(5)

    dst_url = "img/screenshot.png"
    browser.save_screenshot(dst_url)

    return dst_url