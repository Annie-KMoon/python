import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name)
cursor = con.cursor()

#테이블 삭제
sql = "drop table if exists juso"
cursor.execute(sql)
con.commit()

#긴줄 나눠서, 생성
sql  = 'create table juso('
sql += 'seq integer primary key autoincrement,'
sql += 'name char(20),'
sql += 'address char(200))'
cursor.execute(sql)
con.commit()

cursor.close() #커서클로즈
con. close() #컨.클로즈
