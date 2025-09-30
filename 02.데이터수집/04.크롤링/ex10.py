#커피빈-[매장찾기]-매장정보와 이미지 저장/출력하기
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

#java실행-자세히보기창 띄우기
browser.execute_script("storePop2(142)")
time.sleep(5)
#숩생성
soup = BeautifulSoup(browser.page_source,'lxml')

#매장정보찾기(매장명, 매장주소, ) #select(태그)로 찾기, [0]인덱스의 글자만 추출
name = soup.select('div.store_txt > h2')[0].string
info = soup.select('div.store_txt > table.store_table > tbody > tr > td') #매장전체정보에서 [2]는 주소
# address = list(info[2])[0].string #태그가2개라 list화, 그중 0개값
address = info[2].getText()
phone = info[3].string
print('매장이름',name)
print('매장주소', address)
print('매장전화', phone)

#사진불러오기 + 저장(requests 사용)
path = 'data/store'
if not os.path.exists(path):
    os.mkdir(path)
    
imgs = soup.select('div.slick-slide > img')
for img in imgs:
    src ='https://www.coffeebeankorea.com'+img.attrs['src']
    print(src)
    index = src.rindex('/') #/위치를 오른쪽부터 찾는 rindex
    file_name = src[index:]
    print(file_name)

    #이미지저장
    with open(path+file_name, 'wb')as file: #wb 이미지는 바이너리 파일
        res =requests.get(src)
        file.write(res.content) #이미지는 content

#for문으로 전매장 받아오기로 develope
