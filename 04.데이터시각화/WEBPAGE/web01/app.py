#서버 시작 파일은 고정명 app.py
#전역설정
import pandas as pd
df = pd.read_csv('c:/python/04.데이터시각화/data/score.csv', index_col='지원번호')
import matplotlib.pyplot as plt
#한글폰트 설정
plt.rc('font', family = 'Noto Sans KR')
plt.rc('font', size = 15)
plt.rc('axes', unicode_minus = False)


#라이브러리 import-이미지/앱생성
from flask import Flask, render_template, send_file
from io import BytesIO

#앱생성
app = Flask(__name__, template_folder='templates')

#학생별 키 막대그래프 생성 라우트
@app.route('/graph1')
def graph1():
    name = df['이름']
    height = df['키']
    plt.figure(figsize=(10,5))
    plt.ylim(150,210)
    plt.bar(name, height, color='#F0FFF0', ec= '#FAEBD7', hatch = '..')
    plt.xticks(name, rotation=45, size=10, color='gray')
    for idx, h in enumerate(height):
        plt.text(idx, h+1, f'{h}cm', ha='center', color='brown', size=10)
#이미지저장
    img =BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0) #이미지 맨앞으로 이동
    return send_file(img, mimetype='image/png')        


@app.route('/graph2')
def graph2():
    df['평균'] = df.apply(lambda row:row['국어':'사회'].mean(), axis=1)
    name = df['이름']
    avg = df['평균']
    plt.figure(figsize=(10,5))
    plt.ylim(0,100)
    plt.bar(name, avg, color='#B0C4DE', ec= '#F0EBA3', hatch = '--')
    plt.xticks(name, rotation=45, size=10, color='gray')
    for idx, a in enumerate(avg):
        plt.text(idx, a+1, f'{a:.2f}점', ha='center', color='brown', size=10)
#이미지저장
    img =BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0) #이미지 맨앞으로 이동
    return send_file(img, mimetype='image/png')

@app.route('/graph3')
def graph3():
    group = df.groupby('학교')['키'].mean()
    label = group.index
    values = group.values
    plt.figure(figsize=(10,5))
    plt.ylim(160,210)
    plt.bar(label, values, color='#F0EBA3', ec= '#D3D3D3', hatch = '*', width= 0.5)
    plt.xticks(label, rotation=45, size=10, color='gray')
    for idx, v in enumerate(values):
        plt.text(idx, v+1, f'{v:.2f}cm', ha='center', color='brown', size=10)
#이미지저장
    img =BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0) #이미지 맨앞으로 이동
    return send_file(img, mimetype='image/png')

@app.route('/graph4')
def graph4():
    group = df.groupby('학교')['평균'].mean()
    label = group.index
    values = group.values
    plt.figure(figsize=(10,5))
    plt.ylim(0,100)
    plt.bar(label, values, color='#FFE4E1', ec= '#5F9EA0', hatch = '..', width= 0.5)
    plt.xticks(label, rotation=45, size=10, color='gray')
    for idx, v in enumerate(values):
        plt.text(idx, v+1, f'{v:.2f}점', ha='center', color='brown', size=10)
#이미지저장
    img =BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0) #이미지 맨앞으로 이동
    return send_file(img, mimetype='image/png')

@app.route('/graph5')
def graph5():
    df['SW특기'] = df['SW특기'].str.capitalize()
    group = df.groupby('SW특기').size()
    label = group.index
    values = group.values
    plt.figure(figsize=(10,5))
    plt.ylim(0,max(values)+1)
    plt.bar(label, values, color='#DDA0DD', ec= '#A9A9A9', hatch = '--', width= 0.5)
    plt.xticks(label, rotation=45, size=10, color='gray')
    for idx, v in enumerate(values):
        plt.text(idx, v+0.2, f'{v}명', ha='center', color='brown', size=10)
#이미지저장
    img =BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0) #이미지 맨앞으로 이동
    return send_file(img, mimetype='image/png')




#라우트생성
@app.route('/')
def index():
    return render_template('index.html', title='학생관리')

if __name__=='__main__':
    app.run(port=5000, debug=True) 
    #포트넘버설정, 서버로 디버그 즉시반영 설정