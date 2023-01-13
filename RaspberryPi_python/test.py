# image Selector = #islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# search XPATH = /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input

# pip install webdriver-manager selenium# image Selector = #islrg > div.islrc > div:nth-child(2) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# search XPATH = /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input

from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)
input()
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib.request

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)
input()
