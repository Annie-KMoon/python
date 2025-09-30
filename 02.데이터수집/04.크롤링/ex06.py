#[네이버]-[네이버항공]-9월 25일~26일 제주행 항공권 검색-리스트생성
from selenium import webdriver
from selenium.webdriver.common.by import By  #검색어입력
from selenium.webdriver.support.ui import WebDriverWait #대기용
from selenium.webdriver.support import expected_conditions as EC #대기용
# from selenium.webdriver.common.keys import Keys #키값 가져와서 사용
import time
# import re, json

#브라우저생성
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #항상 열림
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
# options.add_argument('headless') #브라우저가 안보이는 상태로 작업가능
#  options.add_argument('window-size=1920x1080') #브라우저 사이즈 지정
browser = webdriver.Chrome(options=options)
browser.maximize_window() #전체윈도우

url = "https://flight.naver.com/"
browser.get(url) #url로 이동
time.sleep(1)

#해당내용을 찾을 때까지 대기 함수 (셀레니움 Wait, EC 추가 임포트)
def waituntil(xpath):
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

#팝업창 7일간 열지 않기 버튼
btn = browser.find_element(By.CLASS_NAME,'FullscreenPopup_suspend')
btn.click()
time.sleep(1)

#가는날 선택 버튼 #Xpath 사용
el = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
el.click()
time.sleep(1)

#25일 버튼(25일이 여러개, 이번달, 인덱스0값)
els = browser.find_elements(By.XPATH, '//b[text()="25"]')
els[0].click()
time.sleep(1)

#26일 버튼
els = browser.find_elements(By.XPATH, '//b[text()="26"]')
els[0].click()
time.sleep(1)

#도착지검색버튼
el = browser.find_element(By.XPATH, '//b[text()="도착"]')
el.click()
time.sleep(1)

#제주 선택 버튼
el = browser.find_element(By.XPATH, '//button[text()="제주"]')
el.click()
time.sleep(1)

#항공권검색 버튼
el = browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
el.click()
time.sleep(1)


#항공권 스케줄 데이터 추출
try:
    #파일저장
    with open('data/flight.txt', 'w', encoding='utf-8') as file:
        first = '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'
        waituntil(first)
        # el = browser.find_element(By.XPATH, first)#검색데이터 1열 텍스트 추출
        # print(el.text)
        els = browser.find_elements(By.CLASS_NAME,'domestic_Flight__8bR_b')
        # print(len(els))
        for idx, el in enumerate(els):
            # print(f'[{idx}] {el.text}')#출력값 확인
            # print(idx+1, '-'*50)
            file.write(f'[{idx}] {el.text}\n')
            file.write('-' * 50)
            file.write('\n')
except:
    pass
finally:
    browser.quit()
    print("프로그램종료!")


# 가는날, 오는날, 도착지 input으로 가능
# 데이터 파일로 저장  