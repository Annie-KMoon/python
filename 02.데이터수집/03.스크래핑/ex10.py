import requests
from bs4 import BeautifulSoup

def weather(city):
    city = city+'날씨' #city 변수값 변동시 검색어에 따라 값 변동
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={city}&ackey=u5uxdxkl'
    res =requests.get(url)
    # print(res) #url req 확인
    soup = BeautifulSoup(res.text, 'lxml')

    #어제보다 #도 높음 텍스트 추출 태그/클래스
    summary = soup.find('p', attrs = {'class':'summary'}).get_text()
    # print(summary)

    #현재온도(텍스트 외 온도값만*온도값태그는 strong)
    temp = soup.find('div', attrs= {'class':'temperature_text'}).strong.contents[1]
    # print(temp)

    #최저 온도
    lowest = soup.find('span', attrs= {'class':'lowest'}).contents[1].replace('°','')
    # print(lowest)

    #최고온도
    highest = soup.find('span', attrs= {'class':'highest'}).contents[1].replace('°','')
    # print(highest)

    print('[오늘날씨]')
    print('-'*50)
    print(summary)
    print(f'현재온도:{temp}도 (최저:{lowest}도 / 최고:{highest}도)')

if __name__=='__main__':
    while True:
        city = input("지역명>")
        if city =="":
            break
        weather(city)    
