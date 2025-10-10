from flask import Blueprint,Flask, render_template, request, send_file
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from io import BytesIO
import numpy as np
import re

from naverapi import getNews
from model import createModel

plt.switch_backend('agg')

bp = Blueprint('news', __name__, url_prefix='/news')

vector, model = createModel()
@bp.route('/predict')
def predict():
    text = request.args['text']
    find_text = re.findall(r'[가-힣]', text)
    join_text = [' '.join(find_text)]
    vector_text = vector.transform(join_text)
    pred = model.predict(vector_text)
    if pred[0]==0:
        return '부정'
    else:
        return '긍정'


@bp.route('/search')
def search():
    page = int(request.args['page'])
    start= (page-1)*5+1 #display
    display=5
    query = request.args['query']
    items, total = getNews(query, start, display)
    data = {'items':items, 'total':total}
    return data

@bp.route('/')
def news():
    return render_template('index.html', pageName = 'news.html', title='AI PM PROJECT')

# if __name__=='__main__':
#     bp.run(port=5000, debug=True)

