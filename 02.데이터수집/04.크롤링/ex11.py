#커피빈-[매장찾기]-전매장 리스트받기
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import re, time 
import requests #사진 저장하기
import os #폴더생성

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_experimental_option('detach', True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

#브라우저 접속
url = "https://www.coffeebeankorea.com/store/store.asp"
browser.get(url)

#전국매장 ID 데이터 수집
store = browser.find_element(By.ID, 'storeListUL')
lis = store.find_elements(By.TAG_NAME, 'li')
lis = [li.get_attribute('data-no') for li in lis]
print(lis)