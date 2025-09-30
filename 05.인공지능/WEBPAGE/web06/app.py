from flask import Flask, render_template, request, send_file
import pandas as pd
import pickle
from tmdbv3api import Movie, TMDb
# from io import BytesIO
# import matplotlib.pyplot as plt
# import numpy as np
# plt.switch_backend('agg')
# from routes import 

#플라스크생성
app = Flask(__name__, template_folder='temp', static_folder='static')

#줄거리 추천 함수
@app.route('/overview/data')
def sim_recommend():
    title = request.args['title'] #프론트에서 title값 받기

    df = pd.read_csv('C:/python/05.인공지능/data/movie/tmdb_5000_movies.csv')
    idx = df[df['title']==title].index[0]

    cosine_sim = pickle.load(open('data/movie/cosine_sim.pickle','rb')) #파일 있을때 리드
    sim = cosine_sim[idx]
    
    sim = list(enumerate(sim))
    sim = sorted(sim, key=lambda x:x[1], reverse=True)
    sim = sim[1:13] #12개값 추출
    index = [x[0] for x in sim]

    tmdb = TMDb() 
    tmdb.api_key='c668cda4cf75bf267ef2aeffa2da0341' 
    tmdb.language='ko-KR' 
    movie = Movie() 

    df = df.loc[index, 'id']
    details = []
    for id in df:
        detail = movie.details(id)
        ko_title = detail['title']
        poster = 'http://image.tmdb.org/t/p/w500' + detail['poster_path']
        overview = detail['overview']
        data = {'title':ko_title, 'poster':poster, 'overview':overview} #dict로 변환
        details.append(data)
    return details


@app.route('/overview')
def overview():
    return render_template('/index.html', pageName='overview.html', title='줄거리추천')

@app.route('/soup')
def soup():
    return render_template('/index.html', pageName='soup.html', title='장르/감독/배우추천')

@app.route('/')
def index():
    pageName = 'home.html'
    return render_template('index.html', pageName=pageName, title='영화추천')

if __name__=='__main__':
    app.run(port=5000, debug=True)

