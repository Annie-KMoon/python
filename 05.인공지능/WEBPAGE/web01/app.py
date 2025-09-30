from flask import Flask, render_template, request, send_file
import pandas as pd
from sklearn.linear_model import LinearRegression, SGDRegressor
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from io import BytesIO
plt.switch_backend('agg')


app = Flask(__name__, template_folder='temp')

def model_linear():
    dataset = pd.read_csv(f'{app.root_path}/data/LinearRegressionData.csv')
    X=dataset.iloc[:, :-1].values
    y=dataset.iloc[:, -1].values
    reg = LinearRegression()
    reg.fit(X,y)
    return reg


#전역변수(계산줄이기)-최소제곱법 모델생성
reg = model_linear()
@app.route('/linear/pred') #최소제곱법 모델생성 예측
def pred_linear():
    hour = int(request.args['hour'])
    pred = reg.predict([[hour]])
    print(pred[0])
    return f'{pred[0]:.2f}'



@app.route('/')
def index():
    pageName = 'home.html'
    return render_template('index.html', pageName=pageName)


@app.route('/linear')
def linear():
    pageName = 'linear.html'
    return render_template('index.html', pageName=pageName)


@app.route('/sgd')
def sgd():
    pageName = 'sgd.html'
    return render_template('index.html', pageName=pageName)


@app.route('/linear/graph')
def graph_linear():
    dataset = pd.read_csv('data/LinearRegressionData.csv')
    dataset.head()
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    plt.scatter(X,y, label='실제점수')
    plt.plot(X, reg.predict(X), label="예측점수", color="g")
    plt.grid(True, ls='--', lw=0.5)
    plt.legend()
    plt.xlabel("공부시간")
    plt.ylabel("시험점수")

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


#경사하강법모델 생성(>노이즈데이터가 있어도 좀더 정확)
@app.route('/sgd/model')
def model_sgd():
    dataset = pd.read_csv(f'{app.root_path}/data/LinearRegressionData.csv')
    X=dataset.iloc[:, :-1].values
    y=dataset.iloc[:, -1].values

    sr = SGDRegressor()
    sr.fit(X,y)
    return sr

sr = model_sgd()

@app.route('/sgd/pred')
def pred_sgd():
    hour = int(request.args['hour'])
    pred = sr.predict([[hour]])
    return f'{pred[0]:.2f}'

@app.route('/sgd/graph')
def graph_sgd():
    dataset = pd.read_csv(f'{app.root_path}/data/LinearRegressionData.csv')
    X=dataset.iloc[:, :-1].values
    y=dataset.iloc[:, -1].values

    plt.scatter(X,y, label='실제점수')
    plt.plot(X, sr.predict(X), label="예측점수", color="g")
    plt.grid(True, ls='--', lw=0.5)
    plt.legend()
    plt.xlabel("공부시간")
    plt.ylabel("시험점수")

    img = BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    return send_file(img, mimetype='image/png')


if __name__=="__main__":
    app.run(port=5000, debug=True)

