from flask import Blueprint,Flask, render_template, request, send_file, jsonify
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from io import BytesIO
import numpy as np
import requests
from bs4 import BeautifulSoup 


plt.switch_backend('agg')

bp = Blueprint('weather', __name__, url_prefix='/weather')

def create_soup(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

@bp.route('/data')
def weather_data():
    query = request.args.get('query', '')
    if not query:
        return jsonify({'error': '검색어가 없습니다.'})

    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&query={query}+날씨'
    soup = create_soup(url)
    if soup is None:
        return jsonify({'error': '데이터를 불러올 수 없습니다.'})
    temp_tag = soup.find('div', attrs={'class': 'temperature_text'})
    temp = temp_tag.get_text(strip=True) if temp_tag else '정보 없음'
    weather_tag = soup.find('span', attrs={'class': 'weather before_slash'})
    weather = weather_tag.get_text(strip=True) if weather_tag else '정보 없음'
    return jsonify({'location': query, 'temperature': temp, 'weather': weather})

@bp.route('/')
def weather():
    return render_template('index.html', pageName = 'weather.html', title='산책날씨체크')


