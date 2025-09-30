#선형회귀 생성모델 함수
def model_linear():
    import pandas as pd
    from sklearn.linear_model import LinearRegression

    dataset = pd.read_csv('data/LinearRegressionData.csv')
    X=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values

    reg = LinearRegression()
    reg.fit(X,y)
    return reg

model = model_linear() 

#시간입력 예측함수
def predict(hour):
    model = model_linear()
    pred = model.predict([[hour]])
    print(f'{hour}시간 공부시 예상 점수는 {pred[0]:.2f}점 입니다.')


while True:
    hour = input("공부시간>")
    if hour =="": 
        break

    elif not hour.isnumeric():
        print("숫자로 입력하세요!")

    else:
        predict(int(hour))