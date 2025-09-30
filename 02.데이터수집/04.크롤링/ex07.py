#기상청-전국날씨-접속(크롤링)-뷰티풀숩(스크래핑)으로 추출
from selenium import webdriver
from bs4 import BeautifulSoup
import re, time  #정규식/시간

date = time.strftime('%Y-%m-%d %H:%M:%S') #시간 포멧

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_experimental_option('detach', True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.weather.go.kr/w/index.do"
browser.get(url)

#크롤링데이터 숩으로 전체 데이터 추출
soup = BeautifulSoup(browser.page_source, 'lxml')
local = soup.find('div',attrs= {'id':'weather2'})
# print(local) 데이터출력확인

#데이터 추출(숩에서 찾은 로컬 사용) 지역별 데이터 추출 (지역별 태그, 클래스 확인)
els = local.find_all('dl', {'class':re.compile('^po_')})
# print(len(els)) #데이터 갯수 확인

print(date) #현재 조회날짜/시간
for idx, el in enumerate(els):
    name = el.dt.getText() #태그 안에 값이 하나일땐
    temp = el.span.getText()
    weather = el.i.getText()
    print(f'{idx+1}){name}, {temp}도, {weather}')
    print('-'*30)