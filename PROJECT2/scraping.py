import requests
from bs4 import BeautifulSoup
import time

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

#날씨
def weather(query):
    url=f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query={query}&oquery=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8&tqi=jMxCDwqVOsVssdnMLaGssssssah-350708&ackey=2zkcsc6k'
    soup = create_soup(url)
    temp = soup.find('div', attrs={'class':'temperature_text'})
    if temp:
        temp = temp.getText()
    else:
        temp = ''
    return temp

#환율
def exchange():
    url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8&ackey=h5qhqyga'
    soup = create_soup(url)
    rate = soup.find('span', attrs={'class':'spt_con dw'}).find('strong') #find 환율만
    if rate:
        rate = rate.getText()
    else:
        rate = ''
    return rate


#주식
def stock(query):
    url=f'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&ssc=tab.nx.all&query={query}&oquery=%EC%82%BC%EC%84%B1%EC%A3%BC%EC%8B%9D&tqi=jMx10sqo1fsssnKt3mosssssteG-036567&acq=%EC%82%BC%EC%84%B1%EC%A3%BC%EC%8B%9D&acr=2&qdt=0&ackey=gr6yvh65'
    soup = create_soup(url)
    price = soup.find('div', attrs={'class':'spt_con dw'}).find('strong') 
    if price:
        price = price.getText()
    else:
        price = ''
    return price

if __name__ == "__main__":
    temp = weather('서울')
    print(temp)