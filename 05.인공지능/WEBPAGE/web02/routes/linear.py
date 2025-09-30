#라우터 생성
from flask import Blueprint, render_template, request #라우터등록정의
from sklearn.linear_model import LinearRegression,SGDRegressor
import pandas as pd

bp = Blueprint('linear', __name__,url_prefix='/linear')

def model_reg():
    dataset = pd.read_csv('data/LinearRegressionData.csv')
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values
    reg = LinearRegression()
    reg.fit(X,y)
    return reg

def model_sgd():
    dataset = pd.read_csv('data/LinearRegressionData.csv')
    X = dataset.iloc[:,:-1].values
    y = dataset.iloc[:,-1].values
    sgd = SGDRegressor()
    sgd.fit(X,y)
    return sgd

#선형회귀 예측결과 라우터
# reg = model_reg()
@bp.route('/reg/pred')
def reg_pred():
    reg = model_reg()
    hour = int(request.args['hour'])
    pred = reg.predict([[hour]])
    return f'{pred[0]:.2f}'

# sgd= model_sgd()
@bp.route('/sgd/pred')
def sgd_pred():
    sgd = model_sgd()
    hour = int(request.args['hour'])
    pred = sgd.predict([[hour]])
    return f'{pred[0]:.2f}'


#최소제곱법 페이지
@bp.route('/reg')
def reg():
    return render_template('index.html', pageName='reg.html',title='최소제곱법(선형회귀)')

#경사하강법 페이지
@bp.route('/sgd')
def sgd():
    return render_template('index.html', pageName='sgd.html',title='경사하강법(선형회귀)')

