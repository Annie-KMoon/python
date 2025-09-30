#WEB03
#전역설정
import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv')

import matplotlib.pyplot as plt

#한글폰트 설정
# plt.rc('font', family = 'Noto Sans KR')
# plt.rc('font', size = 15)
# plt.rc('axes', unicode_minus = False)

#라이브러리 import-이미지/앱생성
from flask import Flask, render_template, send_file
from io import BytesIO

#앱생성
app = Flask(__name__, template_folder='temp')

#라우트생성
@app.route('/')
def index():
    df1 = df[['지원번호','이름','학교','키','SW특기']]
    # df1.set_index('지원번호', inplace=True)

    df2 = df[['지원번호','이름','국어','영어','수학','과학','사회']]
    # df2.set_index('지원번호', inplace=True)

    info = df1.to_html(classes="table table-hover", index=False)
    score = df2.to_html(classes="table table-dark table-hover", index=False)

    return render_template('index.html',info=info, score=score)

if __name__=='__main__':
    app.run(port=5000, debug=True) 
    #포트넘버설정, 서버로 디버그 즉시반영 설정