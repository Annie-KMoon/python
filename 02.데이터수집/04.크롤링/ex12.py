#한빛도서-도서검색
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import re, time 
import requests #사진 저장하기
import os #폴더생성
import json

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_experimental_option('detach', True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

#브라우저 접속
keyword='파이썬'
url = f"https://www.hanbit.co.kr/search/search_list.html?keyword={keyword}"
browser.get(url)

#책 더보기
es = browser.find_element(By.XPATH, '//*[@id="container"]/div[1]/ul/li[3]/a')
es.click()
time.sleep(3)

#데이터 가져오기
soup = BeautifulSoup(browser.page_source, 'lxml')
books = soup.find('div', {'class':'ser_list_wrap'}) #전체 책
books = books.find_all('li', {'class':'ser_bg'})
# print(len(books))

#데이터 파일화
list = []
for book in books:
    no = len(list)+1
    title = book.strong.getText()
    image = book.img['src'] #링크값가져오기
    author = book.span.getText()
    link = 'https://www.hanbit.co.kr' +book.a['href']
    print(title, image,author,link)
    data = {'no':no,'title':title, 'image':image, 'author':author, 'link':link}
    list.append(data)

#json파일에 저장 #어펜드로 하면 추가저장, w으로 하면 대체
with open('data/books.json', 'a', encoding='utf-8')as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)

print("프로그램종료!")