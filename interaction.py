from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = Options()
option.add_experimental_option("detach", True)

#Constants Varibles
TWITTER_USERNAME = "prajwaljung24"
TWITTER_PASSWORD = "Hypeisreal12345@"
PROMISED_UP = 400
PROMISED_DOWN = 400

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
        self.down = 0
        self.up = 0

    def getinternetspeed(self):
        speed = self.driver.get("https://www.speedtest.net/")
        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        start_button.click()
        time.sleep(50)
        up_speed_object = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span")
        self.up = float(up_speed_object.text)
        down_speed_object = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.down = float(down_speed_object.text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/signup")

        #Clicks LOGIN
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]/span/span').click()

        #Enters Username
        time.sleep(3)
        username = self.driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)

        #Clicks NEXT Button
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()

        #Inserts password
        time.sleep(3)
        password = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        #Clicks The Final Login Button
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div").click()
        time.sleep(3)

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            # Clicks The Tweet Button
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div').click()
            time.sleep(2)

            #Tweets about the problem
            tweet = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet.send_keys(f"Hey @ATT, why is my internet speed {self.down}down/{self.up}up?")
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[3]/div/div/div[2]/div[4]/div/span/span').click()

bot = InternetSpeedTwitterBot()
bot.getinternetspeed()
bot.tweet_at_provider()
