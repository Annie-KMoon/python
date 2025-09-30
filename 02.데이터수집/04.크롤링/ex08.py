#기상청-전국 어제 날씨: 현재창에서 숨겨진 내용- [전국]-[어제]를 클릭해야 찾을 수 있음
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import re, time  #정규식/시간

options = webdriver.ChromeOptions()
options.add_argument('headless') #숨김창
# options.add_experimental_option('detach', True)
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.weather.go.kr/w/index.do"
browser.get(url)

#전국 찾기
el = browser.find_element(By.XPATH, '//a[text()="전국"]')
el.click()
time.sleep(1)

#어제 찾기
xpath ='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[1]/a/span'
el = browser.find_element(By.XPATH,xpath)
el.click()
time.sleep(2)

#전체내용 추출
soup = BeautifulSoup(browser.page_source, 'lxml')
local = soup.find('div', {'id':'minmax'})
# print(local)#내용확인

#로컬내용에서 추출
els = local.find_all('dl', {'class':re.compile('^po2_')}) 
# print(len(els))

#어제전국기온 프린트
for idx, el in enumerate(els):
    name = el.dt.getText()
    red = el.find('span',{'class':'red'}).getText()
    blue = el.find('span',{'class':'blue'}).getText()
    print(f'{idx+1}) {name} 최고기온:{red} 최저기온:{blue}')
