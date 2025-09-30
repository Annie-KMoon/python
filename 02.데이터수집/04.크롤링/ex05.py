#크롤링; [쿠팡이동]-[검색어]-[노트북]-[1page 결과출력: 상품이름, 상품가격, 평점..]
from selenium import webdriver
from selenium.webdriver.common.by import By  #검색어입력
from selenium.webdriver.common.keys import Keys #키값 가져와서 사용
import time
import re, json

# options = webdriver.ChromeOptions() #사람이 하는 것으로 에이전트값 지정
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
# browser = webdriver.Chrome(options=options)
# url = "https://www.coupang.com/"
# browser.get(url)

# #검색어 입력창 노트북 입력 명령 변수 생성
# query = browser.find_element(By.NAME, 'q')
# query.send_keys('노트북')

# #검색버튼 누르기 or 키보드 엔터키
# # query.send_keys(Keys.ENTER) #키보드 엔터키 사용 -오류?>>비인간행동으로 막힘..
# time.sleep(100)


#크롤링; [지마켓이동]-[검색어]-[노트북]
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #항상 열림
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window() #전체윈도우

keyword = "노트북"
url = f"https://www.gmarket.co.kr/n/search?keyword={keyword}"
browser.get(url)

# print(browser.page_source) #페이지소스값 프린트, ctrlC로 브레이크
# #페이지 소스 html로 파일 저장
# time.sleep(10)
# with open('data/gmarket.html','w',encoding='utf-8') as file:
#     file.write(browser.page_source)

# time.sleep(5)
# browser.execute_script('alert("..")') #자바경고창 뜨기 명령문도 가능

#스크롤링작업 /  execute_script: 자바스크립트 / 전체 데이터 추출가능:
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(5)

#soup사용
from bs4 import BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')

#검색상품 가져오기(이미지, 타이틀, 가격)
items = soup.find_all('div', attrs = {'class':'box__item-container'})
    # print(len(items)) 상품 갯수 체크

cnt = 0 #구매수5이상리스트,넘버링
list =[] #Json파일화


for idx, item in enumerate(items):
    title = item.find('span', attrs={'class':'text__item'}).getText()
    price = item.find('strong',{'class':'text text__value'}).getText() #attrs 생략가능
    # image = item.find('img') #태그만 찾기>>하단처럼 작성
    # image = 'https:'+item.img['src'] #이미지 한개인경우
    image='https:' + item.find('img', {'class':'image__item'})['src'] #이미지 클래스명상세로 설정
    # count = item.find('li',{'class':'list-item list-item__pay-count'}).getText()#구매수
    # if count ==None:continue >>중복값이 많아서 에러
    link = item.a['href'] #링크값추가
    pay_count = item.find('li',attrs ={'class':re.compile('list-item__pay-count$')}) #li 내 클래스 중복
    if pay_count:
        pay_count = re.sub('구매|건|,','',pay_count.getText()).strip()
        pay_count = int(pay_count)
    else:
        pay_count = 0

    if pay_count >=100: #구매건수 100 이상만 프린트
        cnt += 1
        print(cnt,title,price,image, f'구매건수:{pay_count}')
        #Json파일로 데이터생성
        data = {'no':cnt, 'title':title, 'price':price, 'count':pay_count, 'image':image, 'link':link}
        list.append(data)

#Json파일로 저장(for문 바깥)
with open('data/gmarket.json','w',encoding='utf8')as file:
    json.dump(list, file, indent='\t', ensure_ascii=False)


browser.quit()
print('프로그램종료!')

