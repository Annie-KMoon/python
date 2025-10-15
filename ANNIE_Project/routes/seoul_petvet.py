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

@bp.route('/')
def news():
    # info = df2.to_html(classes='table table-striped table-hover')
    info = df2
    # ✅ 페이지네이션 처리
    infos = info.to_dict(orient='records')
    per_page = 10  # 페이지당 10건
    total = len(infos)

    # 쿼리스트링에서 ?page= 값 가져오기 (없으면 1)
    page = int(request.args.get('page', 1))

    # 페이지 범위 계산
    start = (page - 1) * per_page
    end = start + per_page
    paged_infos = infos[start:end]

    # 페이지 정보 계산
    total_pages = (total + per_page - 1) // per_page  # 올림

    # from pyproj import Transformer
    # transformer = Transformer.from_crs("EPSG:5179", "EPSG:4326", always_xy=True)
    # df2['lon'], df2['lat'] = transformer.transform(df2['좌표정보(X)'], df2['좌표정보(Y)'])

    return render_template('index.html', pageName = 'seoul_petvet.html', title='서울시 동물병원 정보', 
                           page = page, info = paged_infos, total_pages=total_pages)


