import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
db_name = path + '/juso.db'

class Person:
    def __init__(self): #객체 생성
        self.seq = 0
        self.name = "홍길동"
        self.address = "경기도 광명시" #default값

    def print(self): #출력 매서드(함수)생성
        print(f'번호:{self.seq},이름:{self.name},주소:{self.address}')

#목록출력함수
def list(): #모든데이터출력()
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql="select * from juso" #seq,name,address로 별도값 명령도 가능
    cursor.execute(sql)
    rows = cursor.fetchall() #fetchall로 모든 줄
    cursor.close()
    con.close()
    return rows #결과 rows로 리턴

#검색 함수
def search(value):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where name like ? or address like ?"
    value = f'%{value}%'
    # value = '%'+value+'%' #value값 설정
    cursor.execute(sql, (value, value,)) #끝에 꼭,
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

#seq 번호를 받아 읽기 함수
def read(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from juso where seq=?"
    cursor.execute(sql,(seq,))
    row = cursor.fetchone() #한개값 fetchone, row로 변수조정
    cursor.close()
    con.close()
    return row

#삭제 함수
def delete(seq):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "delete from juso where seq=?"
    cursor.execute(sql,(seq,))
    con.commit()
    cursor.close()
    con.close()

#입력 함수
def insert(p):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "insert into juso(name, address) values(?,?)"
    cursor.execute(sql,(p.name, p.address,))
    con.commit()
    cursor.close()
    con.close()

#수정 함수
def update(p):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "update juso set name=?, address=? where seq=?" #데이터 끝에는 ,없이
    cursor.execute(sql,(p.name, p.address,p.seq,))
    con.commit()
    cursor.close()
    con.close()

#테스트
if __name__=="__main__":
    pass
    # #객체생성 테스트
    # person = Person()
    # person.seq = 1
    # person.print() #객체명.def

    # #리스트 테스트
    # rows = list()
    # for row in rows: #리스트 idx 설정
    #     person = Person()
    #     person.seq = row[0]
    #     person.name = row[1]
    #     person.address = row[2]
    #     person.print()

    #검색 테스트
    rows = search('홍')
    for row in rows:
        person = Person()
        person.seq = row[0]
        person.name = row[1]
        person.address = row[2]
        person.print()
    
    # #읽기 테스트
    # row = read(2)
    # p = Person()
    # p.seq = row[0]
    # p.name = row[1]
    # p.address = row[2]
    # p.print()

    # #삭제 테스트
    # seq = int(input("삭제번호>"))
    # row = read(seq)
    # if row == None:
    #     print("삭제 번호가 없습니다.")
        
    # else:
    #     p = Person()
    #     p.seq = row[0]
    #     p.name = row[1]
    #     p.address = row[2]
    #     p.print()
    #     delete(seq)
    #     rows = list()
    #     print(f'데이터 갯수:{len(rows)}')

    # #입력함수
    # rows = list()
    # print(f'입력 전: {len(rows)}')

    # p = Person()
    # p.name = input("이름>")
    # p.address = input("주소>")
    # insert(p)

    # rows = list()
    # print(f'입력 후: {len(rows)}')

    # #수정 테스트
    # p = Person()
    # p.seq = int(input("수정번호>"))
    # row = read(p.seq)
    # if row == None:
    #     print("수정 번호가 없습니다.")
    # else:
    #     p.name = row[1]
    #     p.address = row[2]
    #     name = input(f"이름:{p.name}>")
    #     if name !="": p.name = name
    #     address = input(f"이름:{p.address}>")
    #     if address !="": p.address = address
    #     update(p)
    #     print("수정완료!")