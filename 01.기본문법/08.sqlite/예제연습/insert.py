import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name) #con함수로 sq-연결
cursor = con.cursor() #sql문 실행위한 커서 생성

sql = "insert into juso(name, address) values('강감찬','부산시 동래구')"
cursor.execute(sql) #sql 실행
sql = "insert into juso(name, address) values('홍길동','경기도 광명시')"
cursor.execute(sql) #sql 실행
sql = "insert into juso(name, address) values('이순신','서울 강남구')"
cursor.execute(sql) #sql 실행

id = cursor.lastrowid

con.commit() #커밋
cursor.close() #커서클로즈
con. close() #컨.클로즈

print(f'id:{id}')