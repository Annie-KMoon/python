# #스크래핑
# import requests #인터넷 연결
# from bs4 import BeautifulSoup

# # url = 'https://cgv.co.kr/cnm/cgvChart/movieChart?tabParam=123' #스크래핑할 주소
# # res = requests.get(url) #접속한 결과 응답 res에 저장
# # soup = BeautifulSoup(res.text, 'lxml')
# # # res.raise_for_status()

# # title = soup.title
# # print(title.get_text()) #get_text는 텍스트값만 도출

# url = 'https://www.naver.com/' #스크래핑할 주소
# res = requests.get(url) #접속한 결과 응답 res에 저장
# soup = BeautifulSoup(res.text, 'lxml')

# title = soup.title
# print(1, title.get_text()) #get_text는 텍스트값만 도출

# a = soup.a
# print(2,a) #a태그 가장 앞값
# print(3,a.span.get_text()) #a태그 span 텍스트만
# print(4,a.attrs) #a태그 all
# print(5,a['href']) #a태그 herf


import requests
from bs4 import BeautifulSoup

url='https://www.naver.com/'
res = requests.get(url)

soup = BeautifulSoup(res.text, 'lxml')
title = soup.title

print(1, title)
print(2, title.getText())

title = soup.find('title')
print(3, title)

a = soup.a
print(4, a)

span = a.span
print(5, span.getText())

attrs = a.attrs
print(6, attrs, type(attrs))

href = a['href']
print(7, href)

items = soup.find_all('a')
for item in items:
    print(item.span.getText())