#[네이버]-[네이버항공]-9월 25일~26일 제주행 항공권 검색-리스트생성 : 벡에서 작업 // 
from selenium import webdriver
from selenium.webdriver.common.by import By  #검색어입력
from selenium.webdriver.support.ui import WebDriverWait #대기용
from selenium.webdriver.support import expected_conditions as EC #대기용
import time


#브라우저생성
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #항상 열림
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36')
options.add_argument('headless') #브라우저가 안보이는 상태로 작업가능
browser = webdriver.Chrome(options=options)
browser.maximize_window() #전체윈도우

#해당내용을 찾을 때까지 대기 함수 (셀레니움 Wait, EC 추가 임포트)
def waituntil(xpath):
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))

#이번달 항공권 검색
def flight(start, end, location):
    url = "https://flight.naver.com/"
    browser.get(url) #url로 이동
    time.sleep(1)

    #팝업창 7일간 열지 않기 버튼
    btn = browser.find_element(By.CLASS_NAME,'FullscreenPopup_suspend')
    btn.click()
    time.sleep(1)

    #가는날 선택 버튼 #Xpath 사용
    el = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
    el.click()
    time.sleep(1)

    #start 지정 버튼(25일이 여러개, 이번달, 인덱스0값)
    els = browser.find_elements(By.XPATH, f'//b[text()="{start}"]')
    els[0].click()
    time.sleep(1)

    #end 버튼
    els = browser.find_elements(By.XPATH, f'//b[text()="{end}"]')
    els[0].click()
    time.sleep(1)

    #도착지검색버튼
    el = browser.find_element(By.XPATH, '//b[text()="도착"]')
    el.click()
    time.sleep(1)

    #location 선택 버튼
    el = browser.find_element(By.XPATH, f'//button[text()="{location}"]')
    el.click()
    time.sleep(1)

    #항공권검색 버튼
    el = browser.find_element(By.XPATH, '//span[text()="항공권 검색"]')
    el.click()
    time.sleep(1)


    #항공권 스케줄 데이터 추출
    try:
        with open('data/flight.txt', 'w', encoding='utf-8') as file:
            first = '//*[@id="__next"]/div/main/div[4]/div/div[2]/div[2]/div[1]'
            waituntil(first)
            els = browser.find_elements(By.CLASS_NAME, 'domestic_Flight__8bR_b')
            for idx, el in enumerate(els):  
                file.write(f'[{idx}] {el.text}\n')
                file.write('-'*50)
                file.write('\n')
    except:
        pass
    finally:
        browser.quit()
        print("프로그램종료!")

if __name__=="__main__":
    start = input("가는 날>")
    end = input("오는 날>")
    location = input ("장소명>")
    flight(start, end, location)