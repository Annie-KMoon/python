from flask import Blueprint,Flask, render_template, request, send_file
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from io import BytesIO
import numpy as np
import re


plt.switch_backend('agg')

bp = Blueprint('sds', __name__, url_prefix='/seoul_dogshelter')


@bp.route('/graph1')
def graph1():
    df = pd.read_csv('data/유기동물보호+현황_20251010181858.csv')
    df2 = df[['현황별(2)','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']]
    df2.set_index('현황별(2)', inplace=True)
    years = df2.columns.astype(int)
    dogs = df2.loc['개']
    cats = df2.loc['고양이']
    etc = df2.loc['기타']

    plt.figure(figsize=(10,5))
    plt.plot(years, dogs, marker='o', label='개')
    plt.plot(years, cats, marker='s',ls='--',label='고양이')
    plt.plot(years, etc, marker='x', label='기타')
    # plt.title('유기동물 연도별 현황(2013~2023)', fontsize=20)
    plt.xlabel('연도')
    plt.ylabel('마리 수')
    plt.grid(True, lw=0.5, ls='--')
    plt.legend(loc=(1.02,0))
    for idx, d in enumerate(dogs):
        plt.text(years[idx],dogs[idx]+5,d, ha='center', size=10)
    for idx, c in enumerate(cats):
        plt.text(years[idx],cats[idx]+5,c, ha='center', size=10)
    for idx, e in enumerate(etc):
        plt.text(years[idx],etc[idx]+5,e, ha='center', size=10)

    img =BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close()
    img.seek(0) #이미지 맨앞으로 이동
    return send_file(img, mimetype='image/png')

@bp.route('/')
def news():
    return render_template('index.html', pageName = 'seoul_dogshelter.html', title='서울시유기견현황')