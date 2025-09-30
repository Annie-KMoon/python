import requests
from bs4 import BeautifulSoup

#soup 생성 함수
def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml') #텍스트로 파싱-숩으로 
    return soup


def scrap(section):
#네이버 뉴스 섹션에서 기사 리스트/링크 추출
    url = f'https://news.naver.com/section/{section}'
    soup = create_soup(url)
    news = soup.find('ul', attrs={'class':'sa_list'})
    li = news.find_all('li',limit=5) 
    #5개의 값만
    # print(len(li))
    for idx, item in enumerate(li): #번호붙여 리스트
        title = item.find('strong',attrs={'class':'sa_text_strong'}).getText()
        link = item.find('a')['href'] #a태그, 링크주소 
        print(idx+1, title)
        print(link)

if __name__=='__main__':
    while True:
        section = input("경제:101|사회:102|생활/문화:103|IT/과학:105>")
        if section =="": break
        scrap(section)

