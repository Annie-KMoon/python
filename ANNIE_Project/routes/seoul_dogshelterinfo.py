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

bp = Blueprint('sdsi', __name__, url_prefix='/seoul_dogshelterinfo')

import pandas as pd
from charset_normalizer import from_path

def read_csv_auto(filepath, **kwargs):
    """
    CSV 파일의 인코딩을 자동으로 감지해 pandas DataFrame으로 불러오는 함수

    Parameters:
        filepath (str): CSV 파일 경로
        **kwargs: pd.read_csv()의 추가 옵션 (예: sep, header 등)

    Returns:
        df (pd.DataFrame): 읽어온 데이터프레임
    """

    # 1️⃣ 인코딩 자동 감지
    result = from_path(filepath).best()
    detected_encoding = result.encoding

    print(f"🔍 감지된 인코딩: {detected_encoding}")

    # 2️⃣ 감지된 인코딩으로 CSV 읽기
    try:
        df = pd.read_csv(filepath, encoding=detected_encoding, **kwargs)
    except UnicodeDecodeError:
        print("⚠️ 인코딩 감지 실패 또는 부분 오류 발생. cp949로 재시도합니다.")
        df = pd.read_csv(filepath, encoding='cp949', **kwargs)

    return df

# @bp.route('/data')
# def seoul_dsidata():
#     info = read_csv_auto('data/서울동물복지지원센터 반려동물 입양 정보.csv')
#     import re
#     pattern = r'[^가-힣]+'
#     info['소개내용']=info['소개내용'].apply(lambda x:re.sub(pattern,' ',x))
#     info2 = info[['동물 고유번호','이름','종','성별','출생년도','체중','입양상태','임시보호상태','입소날짜','소개내용']]
#     picture = read_csv_auto('data/서울동물복지지원센터 반려동물 입양 사진.csv')
#     picture2 = picture[['동물 고유번호', '사진url']]
#     picture2_first = picture2.drop_duplicates(subset='동물 고유번호', keep='first')
#     merge = info2.merge(picture2_first, on='동물 고유번호')
#     info = merge.to_html(classes="table table-hover", index=False)
#     return merge

# @bp.route('/')
# def sdsi():
#     info = read_csv_auto('data/서울동물복지지원센터 반려동물 입양 정보.csv')
#     import re
#     pattern = r'[^가-힣]+'
#     info['소개내용']=info['소개내용'].apply(lambda x:re.sub(pattern,' ',x))
#     info2 = info[['동물 고유번호','이름','종','성별','출생년도','체중','입양상태','임시보호상태','입소날짜']]
#     picture = read_csv_auto('data/서울동물복지지원센터 반려동물 입양 사진.csv')
#     picture2 = picture[['동물 고유번호', '사진url']]
#     picture2_first = picture2.drop_duplicates(subset='동물 고유번호', keep='first')
#     merge = info2.merge(picture2_first, on='동물 고유번호')
#     info = merge.to_html(classes='table table-striped table-hover')

#     return render_template('index.html', pageName = 'seoul_dogshelterinfo.html', title='서울동물복지지원센터입양정보', info=info)

@bp.route('/')
def sdsi():
    import re
    info = read_csv_auto('data/서울동물복지지원센터 반려동물 입양 정보.csv')
    pattern = r'[^가-힣]+'
    info['소개내용'] = info['소개내용'].apply(lambda x: re.sub(pattern, ' ', str(x)))

    info2 = info[['동물 고유번호','이름','종','성별','출생년도','체중','입양상태','임시보호상태','입소날짜']]
    picture = read_csv_auto('data/서울동물복지지원센터 반려동물 입양 사진.csv')
    picture2 = picture[['동물 고유번호', '사진url']]

    picture2_first = picture2.drop_duplicates(subset='동물 고유번호', keep='first')
    merge = info2.merge(picture2_first, on='동물 고유번호')

    # ✅ 페이지네이션 처리
    animals = merge.to_dict(orient='records')
    per_page = 10  # 페이지당 10건
    total = len(animals)

    # 쿼리스트링에서 ?page= 값 가져오기 (없으면 1)
    page = int(request.args.get('page', 1))

    # 페이지 범위 계산
    start = (page - 1) * per_page
    end = start + per_page
    paged_animals = animals[start:end]

    # 페이지 정보 계산
    total_pages = (total + per_page - 1) // per_page  # 올림

    return render_template(
        'index.html',
        pageName='seoul_dogshelterinfo.html',
        title='서울동물복지지원센터 입양정보',
        animals=paged_animals,
        page=page,
        total_pages=total_pages
    )