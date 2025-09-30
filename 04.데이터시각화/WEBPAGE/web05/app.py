#WEB05
#전역설정
import pandas as pd
import matplotlib.pyplot as plt

#한글폰트 설정
plt.rc('font', family = 'Malgun Gothic')
plt.rc('font', size = 5)
plt.rc('axes', unicode_minus = False)

#라이브러리 import-이미지/앱생성
from flask import Flask, render_template, send_file, request
from io import BytesIO

#앱생성 #temp:html
app = Flask(__name__, template_folder='temp')

#라우트생성
@app.route('/')
def health():
    return render_template('health.html')


#데이터라우트생성
@app.route('/health/data')
def health_data():
    import pandas as pd
    page = int(request.args['page'])
    # print(page)
    size = int(request.args['size'])
    word = request.args['word']

    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')
    filt = df['시도군구'].str.contains(word)
    df = df[filt]

    start = (page-1)*size
    end = page*size
    df2 = df[start:end]
    count = len(df)
    table = df2.to_html(index=True, classes='table table-dark table-striped-columns')

    data = {'count':count, 'table':table}
    return data

#그래프생성라우트
@app.route('/health/graph')
def health_graph():
    df = pd.read_csv(f'{app.root_path}/data/인구수별공공의료기관수.csv')
    word=request.args['word']
    filt = df['시도군구'].str.contains(word)
    df = df[filt]
    if len(df)>10:
        df = df[:10]

    plt.title("지역별 공공의료기관수", size=20)
    plt.barh(df['시도군구'], df['count'], color='gray')
    # for idx, count in enumerate(df['count']):
    #     plt.text(count+0.5, idx, count, va='center')
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__=='__main__':
    app.run(port=5000, debug=True) 