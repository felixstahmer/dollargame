from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver 

import time

class GameController(): 
    def __init__(self):
        url = "https://thedollargame.io/game/level/100/100/1"
        # BASE_DIR = "activegame"
        chromedriver = "/usr/local/bin/chromedriver"
        

        # options = Options();
        # options.addArguments("--start-maximized");

        global browser

        chrome_options = Options()
        chrome_options.add_argument("--kiosk");
        # chrome_options.add_argument("window-size=1400,1020")
        chrome_options.add_experimental_option("detach", True)

        self.browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
        # self.browser.set_window_size(1500, 1200)
        # self.browser.maximize_window()
        # self.browser.fullscreen_window()

        self.browser.get(url)

        time.sleep(5)  # wait 5 seconds for the site to load.
        self.el = self.browser.find_element_by_id("root")
        self.action = ActionChains(self.browser)
        self.skip_tutorial()

    def skip_tutorial(self):
        tutorial_button_classname = "Hint_SkipBtn__2HsyR"
        self.click_button(tutorial_button_classname)
        time.sleep(2)
        
    def click_next_level_button(self):
        time.sleep(5)
        button_for_next_level = "BackBtn_BackBtn__KQPMr"
        self.click_button(button_for_next_level)
        time.sleep(5)

    def click_button(self, classname):
        try:
            button = self.browser.find_element(By.CLASS_NAME, classname)
            button.click()
        except NoSuchElementException:
            print("Button not Found")
    
    def take_screenshot(self, dst_url_for_sreenshot):
        self.browser.save_screenshot(dst_url_for_sreenshot)

    def play(self, nodes): 
        for node in nodes.node_list: 
            for i in range(node.amount_of_clicks):
                self.action.move_to_element_with_offset(self.el, node.x, node.y)
                self.action.click()
                self.action.perform()
                time.sleep(1)

