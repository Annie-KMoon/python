# import requests
# from bs4 import BeautifulSoup

# #[네이버]-[네이버증권]-[top종목]-[거래상위]
# url = "https://finance.naver.com/"
# res =requests.get(url)

# soup = BeautifulSoup(res.text, 'lxml')
# items = soup.find('tbody', attrs = {'id':'nxt_topItems1'})

# #1위값
# rank1 = items.find('tr') #1번째 tr값
# print(1, rank1.a.get_text())

# #2위값
# # rank2 = rank1.next_sibling.next_sibling #2번째 tr값(역슬래시가 하나 있어서)
# rank2 = rank1.find_next_sibling('tr')
# print(2, rank2.a.get_text())

# #2위값기준 1위값
# rank1 = rank2.find_previous_sibling('tr')
# print(1,rank1.a.get_text())

# #전체값
# siblings = rank1.find_next_siblings('tr')
# print(3,len(siblings))

# #siblings 값으로 -배열의 1기준 2번부터 0
# rank2 = siblings[0]
# print(4,rank2.a.get_text())
# rank3 = siblings[1]
# print(5,rank3.a.get_text())

# #부모값(items) 기준
# rank = items.find_all('a') #아이템 안의 a
# print(6, len(rank))

# #부모값(items) 기준, #실시간 값 변동 *이방식으로 제일 많이 사용
# ranks = items.find_all('tr') #아이템 안의 tr
# print(7, len(ranks)) #갯수
# for index, rank in enumerate(ranks):#전체리스트 인덱스값설정하여 추출
#     print(index+1, rank.a.get_text())

# #price값 가져오기 (홈페이지, 'td'에 가격 값 확인)
# for index, rank in enumerate(ranks):
#     price = rank.find_all('td')[0].get_text() #이름+값 추출
#     print(index+1, rank.a.get_text(), price)

# #up&down값 가져오기 (홈페이지, 'td'에 가격 값 확인)
# for index, rank in enumerate(ranks):
#     td = rank.find_all('td')
#     price = td[0].get_text()
#     up_down = td[2].get_text().strip() #strip() 공백제거
#     print(index+1, rank.a.get_text(),price, up_down)


import requests
from bs4 import BeautifulSoup

url='https://finance.naver.com/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

#[Top종목]-[거래상위]
tbody = soup.find('tbody', attrs={'id':'_topItems1'})
trs = tbody.find_all('tr')

list = []
for idx, tr in enumerate(trs):
    up_down = tr['class']
    name = tr.a.getText()
    tds = tr.find_all('td')
    price = tds[0].getText()
    up_down_price=tds[1].getText().replace('하락','').replace('상승','').strip()
    #print(idx+1, name, price, up_down[0], up_down_price)
    list.append(f'{idx+1},{name},{price},{up_down[0]},{up_down_price}')
print(list)

#텍스트파일생성
file_name = 'data/거래상위.txt'
with open(file_name, 'w', encoding='utf-8') as file:
    for line in list:
        file.write(line + '\n')