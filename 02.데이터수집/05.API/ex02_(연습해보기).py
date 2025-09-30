#서울지역 식신로드 만점식당 20선

import requests
from bs4 import BeautifulSoup

def getAddress():
    url='https://www.wikitree.co.kr/articles/217101'
    res =requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')


if __name__=="__main__":
    getAddress()