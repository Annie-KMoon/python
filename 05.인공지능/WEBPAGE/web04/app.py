from flask import Flask, render_template
from routes import linear, multi, poly,logistic #라우터등록

app = Flask(__name__, template_folder='temp')
app.register_blueprint(linear.bp) #라우터등록
app.register_blueprint(multi.bp) #라우터등록
app.register_blueprint(poly.bp) #라우터등록
app.register_blueprint(logistic.bp) #라우터등록

@app.route('/')
def index():
    pageName = 'home.html'
    return render_template('index.html', pageName=pageName, title='자기소개')

if __name__=='__main__':
    app.run(port=5000, debug=True)

