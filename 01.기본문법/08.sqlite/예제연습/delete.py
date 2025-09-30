import sqlite3
import os

path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

con = sqlite3.connect(db_name) #con함수로 sq-연결
cursor = con.cursor() #sql문 실행위한 커서 생성

sql = "delete from juso where seq=?" #모를 땐 ?
seq = int(input("삭제번호>")) #seq=삭제번호
cursor.execute(sql, (seq,)) #삭제번호 뒤에 , 양식주의
con.commit()

cursor.close() #커서클로즈
con. close() #컨.클로즈