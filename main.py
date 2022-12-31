from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from logger import setup_logger
from helpers import GH_TOKEN
from time import sleep
import os
os.environ["GH_TOKEN"]=GH_TOKEN
logger = setup_logger()
logger.info("logger is setup")

opts = FirefoxOptions()
opts.add_argument("--headless")
opts.add_argument("maximize_window")
opts.set_preference("general.useragent.override", UserAgent().random)

service = FirefoxService(GeckoDriverManager().install())

url = 'https://books.toscrape.com'
driver = webdriver.Firefox(service=service, options=opts)
driver.get(url)
driver.maximize_window()
sleep(5)
logger.info("driver maximized")
books = driver.find_elements(By.TAG_NAME, 'article')
print(f'There are {len(books)} books on that page')

driver.close()