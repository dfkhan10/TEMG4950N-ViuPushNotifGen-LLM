import requests
from bs4 import BeautifulSoup
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def find_ins_profile(cast):
    query = f"{cast} official Instagram"
    for j in search(query, num_results=10, sleep_interval=5):
        if "instagram.com" in j and "?hl=en" in j:
            print(j)
            return j
        else:
            return None
        
def login_to_ig():
    USERNAME = "temg4950nig@gmail.com"
    PASSWORD = "TEMGISAMAZING"

    wd_path = "C:\\Users\\charl\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"
    
    service = Service(wd_path)
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)

        password_input.send_keys(Keys.RETURN)
    finally:
        time.sleep(5)
        driver.quit()

login_to_ig()

def scrap_ig_post(url):
    wd_path = "C:\\Users\\charl\\Downloads\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe"
    
    service = Service(wd_path)
    wdriver = webdriver.Chrome(service=service)

    wdriver.get(url)
    time.sleep(5)

    try:
        # Retrieve all anchor tags
        links = wdriver.find_elements(By.TAG_NAME, 'a')

        posts = []
        for link in links:
            post = link.get_attribute('href')
            if "/p/" in post:
                posts.append(post)
                print(post)

        # print(href)

    finally:
        # Clean up and close the driver
        wdriver.quit()


find_ins_profile("lee joo-bin")

#scrap_ig_post("https://www.instagram.com/hellobeen/?hl=en")


#from ntscraper import Nitter

#scraper = Nitter()

#tweets = scraper.get_tweets('elonmusk', mode='user', number=5)

#print(tweets)

# from twikit import Client, TooManyRequests
# from datetime import datetime
# from configparser import ConfigParser
# from random import randint
# import asyncio

# # MINIMUM_TWEES = 5
# # QUERY = "chatgpt"

# # config = ConfigParser()
# # config.read("config.ini")
# # username = config['X']['username']
# # email = config['X']['email']
# # password = config['X']['password']

# # client = Client(language='en-US')
# # client.login(auth_info_1=username, auth_info_2=email, auth_info_3=password)
# # #client.save_cookies('cookies.json')

# # #client.load_cookies('cookies.json')

# # #get Tweets
# # tweets = client.get_tweet(QUERY, product='Top')#

# # for tweet in tweets:
# #     print(vars(tweet))
# #     break

# client = Client('en-US')

# async def main():
#     await client.login(
#         auth_info_1='temg4950n',
#         auth_info_2='temg4950nig@gmail.com',
#         password='TEMGISAMAZING'
#     )

# asyncio.run(main())