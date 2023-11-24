from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

# Constants
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Find and click on GO button:
        self.driver.find_element(by=By.XPATH,
                                 value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        time.sleep(60)

        # Get download speed text:
        self.down = self.driver.find_element(by=By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                   '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        # Get upload speed text:
        self.up = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                 '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # Print text to the console:
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        # Convert upload and download speed to float in order to compare:
        float_down = float(self.down)
        float_up = float(self.up)

        # Compare speed with promised speed:
        if float_down < PROMISED_DOWN or float_up < PROMISED_UP:
            self.driver.get("https://twitter.com/")

            # Find and click Sign in button
            self.driver.find_element(by=By.XPATH,
                                     value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div['
                                           '3]/div[5]/a').click()
            time.sleep(10)
            # Get phone field:
            phone_field = self.driver.find_element(by=By.XPATH,
                                                   value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                         '2]/div/input')
            # Enter phone_no into phone field:
            phone_field.send_keys(os.getenv('TWITTER_PHONE_NO'))
            # Hit Enter:
            phone_field.send_keys(Keys.ENTER)
            time.sleep(3)
            # Get password field:
            password_field = self.driver.find_element(by=By.XPATH,
                                                      value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                            '2]/div/label/div/div[2]/div[1]/input')
            # Enter password into password_field:
            password_field.send_keys(os.getenv('TWITTER_PASSWORD'))
            # Hit enter:
            password_field.send_keys(Keys.ENTER)
            time.sleep(20)

            # Get field for composing a tweet:
            tweet_compose = self.driver.find_element(by=By.XPATH,
                                                     value='//div[@data-testid="tweetTextarea_0"]')

            tweet_message = f"Hey Internet Service Provider, why is my internet speed {float_down}down/{float_up}up " \
                            f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up"
            time.sleep(20)
            # Send tweet message to the compose field:
            tweet_compose.send_keys(tweet_message)
            time.sleep(5)
            # Get button for posting a tweet:
            post = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div['
                                                               '2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div['
                                                               '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div['
                                                               '2]/div[3]')
            # Hit the button:
            post.click()
            time.sleep(10)

            self.driver.close()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
