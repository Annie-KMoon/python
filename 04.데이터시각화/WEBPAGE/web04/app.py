#WEB04
#전역설정
import pandas as pd
import matplotlib.pyplot as plt

# 한글폰트 설정
plt.rc('font', family = 'Noto Sans KR')
plt.rc('font', size = 8)
plt.rc('axes', unicode_minus = False)

#라이브러리 import-이미지/앱생성
from flask import Flask, render_template, send_file, request
from io import BytesIO

#앱생성
app = Flask(__name__, template_folder='temp')

#라우트생성1 데이터출력
@app.route('/score')
def score():
    return render_template('score.html')

#라우트생성2 데이터생성 라우터
@app.route('/score/data')
def score_data():
    word = request.args['word']
    # print(word)

    df = pd.read_csv('C:/python/04.데이터시각화/WEBPAGE/web04/static/score.csv')
    # df = pd.read_csv(f'{app.root_path}/static/score.csv')

    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)

    filt = (df['이름'].str.contains(word)) | (df['학교'].str.contains(word))
    df = df[filt]

    df_info = df[['지원번호', '이름','학교','키','SW특기']]
    df_score = df[['지원번호', '이름','국어','영어','수학','과학','사회','평균']]
    
    table_info = df_info.to_html(classes="table table-hover", index=False)
    table_score = df_score.to_html(classes="table table-dark table-hover", index=False)
    data={'info':table_info, 'score':table_score}
    return data

@app.route('/score/graph')
def score_graph():
    df = pd.read_csv('C:/python/04.데이터시각화/WEBPAGE/web04/static/score.csv')
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    plt.bar(df['이름'], df['평균'], color='gray')
    xticks=[f'{df.loc[x,"이름"]}\n({df.loc[x,"지원번호"]})'for x in range(len(df))]
    plt.xticks(df['이름'], xticks)

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__=='__main__':
    app.run(port=5000, debug=True) 