from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        # Login to Instagram:
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        # Get username field and send your username:
        username_field = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(os.getenv('USERNAME'))

        # Get password field, send in your password and hit enter:
        password_field = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(os.getenv('PASSWORD'))
        password_field.send_keys(Keys.ENTER)
        sleep(10)

    def find_followers(self):
        # Go to the page you wish to follow:
        self.driver.get(f"https://www.instagram.com/{os.getenv('SIMILAR_ACCOUNT')}")
        sleep(10)
        # Find and click on the list of followers:
        followers_list = self.driver.find_element(by=By.CSS_SELECTOR, value="a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd"
                                                                            ".xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2"
                                                                            ".xe8uvvx.xdj266r.x11i5rnm.xat24cr"
                                                                            ".x1mh8g0r.xexx8yu.x4uap5.x18d9i69"
                                                                            ".xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq"
                                                                            ".x1a2a7pz._alvs._a6hd")
        followers_list.click()
        sleep(10)

    def follow(self):
        # Find popup window in order to be able to scroll:
        popup = self.driver.find_element(by=By.CSS_SELECTOR, value='div._aano')
        sleep(3)

        scroll_count = 10  # Number of times scrolling will be performed
        for _ in range(scroll_count):
            # Scroll the window:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
            sleep(2)

            # Find all the elements containing the follow button:
            all_buttons = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.x9f619.x1n2onr6.x1ja2u2z.xdt5ytf"
                                                                              ".x2lah0s.x193iq5w.xeuugli.xamitd3"
                                                                              ".x78zum5 button._acan._acap._acas._aj1-")
            # Loop to click each button in all buttons:
            for button in all_buttons:
                print("called")

                # Exception handling incase you are already following the user:
                try:
                    button.click()
                    sleep(1)

                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button._a9--._a9_1")
                    cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
