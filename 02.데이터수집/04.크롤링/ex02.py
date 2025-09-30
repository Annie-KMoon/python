from selenium import webdriver
from selenium.webdriver.common.by import By #아이디 등 클래스네임 가져오기
from selenium.webdriver.common.keys import Keys #아이디, 비번 입력
import time #타임임포트하여 기능 이용/ 브라우저창 자동닫힘이기때문에

#브라우저 생성
browser = webdriver.Chrome()
browser.get('https://www.naver.com/')

#로그인버튼클릭
button = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
button.click()
time.sleep(2)

#아이디입력
id = browser.find_element(By.ID, 'id')
id.send_keys('mkw005')
time.sleep(2)

#비번입력
pw = browser.find_element(By.ID, 'pw')
pw.send_keys('')
time.sleep(2)

#로그인
login = browser.find_element(By.ID,'log.login')
login.click()

time.sleep(100)