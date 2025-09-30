import requests
from bs4 import BeautifulSoup
import csv

file_name = 'data/할리스매장.csv'
file = open(file_name, 'w', encoding='utf-8-sig', newline='') #결과 저장 파일 생성
writer = csv.writer(file)

title=['NO', '지역명', '매장명', '주소', '전화'] #타이틀지정
writer.writerow(title)

#[할리스 커피]-[Store]-[매장검색]
for page in range(1,11): #1~10페이지반복
    url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=서울&gugun=&store='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')

    table = soup.find('table', attrs={'class':'tb_store'})
    rows = table.find_all('tr')
    for idx, row in enumerate(rows):
        if idx==0:continue
        cols = row.find_all('td') #매장정보
        # print(cols)-정보순서체크
        city = cols[0].getText().strip()
        name = cols[1].getText().strip()
        address = cols[3].getText().replace(',',' ').replace('.','').strip()
        phone = cols[5].getText().strip().replace('.','')
        data = [idx*page, city, name, address, phone] #매장정보를 list 자료형에 저장
        writer.writerow(data)
