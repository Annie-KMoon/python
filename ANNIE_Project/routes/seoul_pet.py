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

bp = Blueprint('sp', __name__, url_prefix='/seoul_pet')

@bp.route('/')
def news():
    return render_template('index.html', pageName = 'seoul_pet.html', title='서울시 반려동물 통계')