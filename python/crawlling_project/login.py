from selenium.webdriver.common.alert import Alert
from setting import chrome_driver
import time
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import random

if __name__ == "__main__":
    url = 'https://www.coffeebeankorea.com/member/login.asp'
    driver = chrome_driver()
    driver.get(url)
    time.sleep(random.uniform(1, 4))
    username = driver.find_element(By.XPATH, """//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[1]/input""")
    password = driver.find_element(By.XPATH, """//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/div/p[2]/input""")
    username.send_keys("an9383")
    time.sleep(random.uniform(1, 4))
    password.send_keys("Sa9200502^")
    time.sleep(random.uniform(1, 4))
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/fieldset/div/div[1]/div[1]/a').click()
    time.sleep(random.uniform(1, 10))
    driver.find_element(By.XPATH, """//*[@id="gnb"]/ul/li[3]/a""").click()
    time.sleep(random.uniform(1, 10))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(random.uniform(1, 10))
    driver.find_element(By.LINK_TEXT, "2").click()
    time.sleep(random.uniform(1, 10))

