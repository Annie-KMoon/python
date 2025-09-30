import requests
from bs4 import BeautifulSoup
import os

path = os.getcwd() + '/data/books'
if not os.path.exists(path):
    os.mkdir(path) #파일디렉터리생성(폴더생성)

url='https://www.hanbit.co.kr/store/store_submain.html'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

section = soup.find('ul', attrs={'id':'new_books_slider'})
imgs = section.find_all('img') #이미지다운로드

for idx, img in enumerate(imgs):
    url = img['src']
    res_img = requests.get(url)
    file_name=path + f'/book{idx+1:02d}.jpg'
    with open(file_name, 'wb') as file: #wb?
        file.write(res_img.content)