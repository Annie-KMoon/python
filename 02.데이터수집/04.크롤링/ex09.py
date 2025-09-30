#기상청-전국-[예보]
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import re, time  #정규식/시간

options = webdriver.ChromeOptions()
options.add_argument('headless')
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

#예보 찾기 (#span, a 태그로 xpath)
xpath ='//*[@id="content-body"]/div[4]/div/div/div[1]/ul/li[3]/a/span'
el = browser.find_element(By.XPATH,xpath)
el.click()
time.sleep(1)

for i in range(1,8): #1~7반복
    xpath=f'//*[@id="local-weather"]/div/div[{i}]/h3/a'
    el = browser.find_element(By.XPATH, xpath)
    title = el.text.replace('\n','')
    print(f'---------------{title}------------------')
    el.click()
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source, 'lxml')
    local = soup.find('div', {'id':'weather'})
    els = local.find_all('dl', re.compile('^po_'))
    for el in els:
        name = el.dt.getText()
        temp = el.span.getText()
        weather = el.i.getText()
        print(name, temp, weather)
