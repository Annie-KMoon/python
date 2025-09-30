from selenium import webdriver

#웹드라이버 옵션 / 브라우저창 닫히지 않게 성정
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True) #브라우저창이 항상 오픈
browser = webdriver.Chrome(options=options)
browser.maximize_window() #전체창으로 크게

#브라우저창이동
url = 'https://flight.naver.com'
browser.get(url)

#스크린샷 저장
browser.get_screenshot_as_file('data/flight.png')

#브라우저 종료
browser.quit()