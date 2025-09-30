from selenium import webdriver
from selenium.webdriver.common.by import By #아이디 등 클래스네임 가져오기
import time #타임임포트하여 기능 이용

#크롬브라우져 생성
browser = webdriver.Chrome()
browser.get('https://www.naver.com')

#로그인버튼-클릭 동작 지정
button = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
button.click()

time.sleep(3) #3초동안 프로그램정지

#뒤로가기
browser.back()

#이전으로 가기
browser.forward()

#새로고침
browser.refresh()

time.sleep(10) #10초동안 프로그램정지 후 종료