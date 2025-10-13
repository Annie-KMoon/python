from flask import Blueprint,Flask, render_template, request, send_file, jsonify
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from io import BytesIO
import numpy as np
import re

plt.switch_backend('agg')

bp = Blueprint('spv', __name__, url_prefix='/seoul_petvet')
df = pd.read_csv('data/서울시 동물병원 인허가 정보.csv', encoding='ANSI')
df2 = df[['관리번호','사업장명','도로명주소','상세영업상태명','좌표정보(X)','좌표정보(Y)']]

@bp.route('/search')
def search():
    name = request.args.get('name', '').strip()
    if not name:
        return jsonify([])

    # 부분 일치 검색
    results = df2[df2['사업장명'].str.contains(name, case=False, na=False)]
    vets = results[['사업장명', '도로명주소', '좌표정보(X)','좌표정보(Y)']].to_dict(orient='records')
    return jsonify(vets)

@bp.route('/')
def news():
    info = df2.to_html(classes='table table-striped table-hover')
    return render_template('index.html', pageName = 'seoul_petvet.html', title='서울시 동물병원 정보', info=info)


