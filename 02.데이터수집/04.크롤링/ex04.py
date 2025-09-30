from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless') #브라우저가 안보이는 상태로 작업가능
# options.add_argument('window-size=1920x1080') #브라우저 사이즈 지정

#브라우저 생성
browser = webdriver.Chrome(options=options)

#브라우저 접속
url = 'https://flight.naver.com'
browser.get(url)

#스크린샷 저장
browser.get_screenshot_as_file('data/flight3.png')