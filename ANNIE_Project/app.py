from flask import Flask, render_template, request, send_file
import re
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from naverapi import getNews
from model import createModel

import routes.news as news
import routes.seoul_dogshelterinfo as sdsi
import routes.seoul_dogshelter as sds
import routes.seoul_petvet as spv
import routes.seoul_pet as sp



#플라스크생성
app = Flask(__name__, template_folder='temp', static_folder='static')
app.register_blueprint(news.bp) 
app.register_blueprint(sdsi.bp) 
app.register_blueprint(sds.bp) 
app.register_blueprint(sp.bp) 
app.register_blueprint(spv.bp) 

@app.route('/')
def index():
    return render_template('index.html', pageName = 'home.html', title='AI PM PROJECT')

if __name__=='__main__':
    app.run(port=5000, debug=True)

