from flask import Flask, render_template, request
import pandas as pd

#플라스크생성
app = Flask(__name__, template_folder='temp', static_folder='static')

@app.route('/predict')
def predict():
    from sklearn.neighbors import KNeighborsClassifier
    model = KNeighborsClassifier()

    test = pd.read_csv('data/타이타닉/테스트.csv')
    train = pd.read_csv('data/타이타닉/훈련.csv')
    X=train.iloc[:, 1:].values
    y=train.iloc[:, 0].values
    model.fit(X,y)

    X_pred = test.iloc[:, :].values
    y_pred = model.predict(X_pred)

    df_test = pd.read_csv('data/타이타닉/test.csv')
    df_test['pred'] = y_pred
    df_test.head(5)

@app.route('/data')
def data():
    page = int(request.args['page'])
    size = int(request.args['size'])
    start = (page-1)*size #0, 5, 10
    end = (page*size) #4, 9, 14
    df = pd.read_csv('data/타이타닉/test.csv')
    cols=['Name', 'Sex', 'Age', 'Fare', 'Pclass', 'Embarked']
    df = df[cols]
    df.columns = ['성명','성별','나이','요금','등급','항구']
    total = len(df)
    df = df[start:end]
    table = df.to_html(classes='table table-dark table-striped-columns', index=False)
    
    data={'table':table, 'total':total}    #dict-json
    return data
   
@app.route('/')
def index():
    return render_template('index.html', pageName = 'home.html', title='타이타닉 생존예측')

if __name__=='__main__':
    app.run(port=5000, debug=True)

