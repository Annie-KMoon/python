from flask import Blueprint,Flask, render_template, request, send_file
import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rc('axes',unicode_minus=False)
from io import BytesIO
import numpy as np
import re


plt.switch_backend('agg')

bp = Blueprint('weather', __name__, url_prefix='/weather')

@bp.route('/')
def news():
    return render_template('index.html', pageName = 'weather.html', title='산책날씨체크')