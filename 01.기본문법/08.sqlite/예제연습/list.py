import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name) #con함수로 sq-연결
cursor = con.cursor() #sql문 실행위한 커서 생성

# sql = "select * from juso where address like '%경%' order by seq desc"
sql = "select * from juso"
cursor.execute(sql)

rows = cursor.fetchall() #커서의 모든 결과 출력(여러줄)
for row in rows:
    print(f'번호:{row[0]},이름:{row[1]},주소:{row[2]}') #row idx no

cursor.close() #커서클로즈
con. close() #컨.클로즈    