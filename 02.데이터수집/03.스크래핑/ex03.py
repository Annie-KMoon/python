# import requests
# from bs4 import BeautifulSoup

# #[네이버]-[네이버증권]-[인기종목]
# url = "https://finance.naver.com/"
# res =requests.get(url)

# soup = BeautifulSoup(res.text, 'lxml')
# top5 = soup.find('div', attrs = {'class':'aside_area aside_popular'})
# # table = top5.find('table')
# # trs = table.find_all('tr')
# names = top5.find_all('a')
# print(len(names))

# # for item in items:
# #     title = item.get_text()
# #     print(title)

# #이름추출
# for name in names:
#     print(name.get_text())



import requests
import csv #엑셀파일화
from bs4 import BeautifulSoup
import re #정규표현식, match, fullmatch, search 등 사용가능

#파일로 저장
file_name ='data/코스닥거래상위1~100.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(file)

#[Top종목]-[거래상위]-[더보기]-[코스닥]
url='https://finance.naver.com/sise/sise_quant.naver?sosok=1'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

table = soup.find('table', attrs={'class':'type_2'})
rows = table.find_all('tr')


#?
for row in rows:
    cols = row.find_all('td')
    if len(cols) <=1 :continue
    data = [re.sub('\t|\n|하락|상승|보합','', col.getText()) for col in cols] #리스트로 전환
    # print(data)
    writer.writerow(data)