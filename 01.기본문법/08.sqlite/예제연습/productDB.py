import sqlite3
import os
path = os.path.dirname(os.path.realpath(__file__))
# print(path) 패쓰 확인
db_name = path + '/juso.db' #jusodb에 product시트로 사용, sqlite 에서 생성완

#클래스 생성
class Product:
    def __init__(self):
        self.code=0
        self.name=""
        self.price=0

    def print(self):
        print(f"코드:{self.code}, 상품명:{self.name}, 상품가격:{self.price:,}원")

#row 출력 함수
def rowPrint(row):
    if row == None:
        print("해당 상품이 없습니다.")
    else:
        p = Product()
        p.code = row[0]
        p.name = row[1]
        p.price = row[2]
        p.print()
        return p
    
def rowPrint2(row):
    p = Product()
    p.code = row[0]
    p.name = row[1]
    p.price = row[2]
    p.print()
    return p


#리스트함수(타입별 정렬옵션)
def list(type): #type=1:코드순, 2:이름순, 3:최저가, 4:최고가
    con = sqlite3.connect(db_name) #db 오픈
    cursor=con.cursor() #커서 오픈
    sql='select * from product ' #select code, name, price from product/ product 뒤에 공백체크*
    if type ==1:
        sql += 'order by code'
    elif type ==2:
        sql += 'order by name' 
    elif type ==3:
        sql += 'order by price'
    elif type ==4:
        sql += 'order by price desc' #desc 내림차순
    cursor.execute(sql)
    rows = cursor.fetchall() #값 여러가지 fetchall
    cursor.close()
    con.close()
    return rows #결과처리

#입력 함수
def insert(p): #p.객체로 설정/클래스 우선 설정
    con=sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "insert into product(name, price) values(?,?)"
    cursor.execute(sql,(p.name, p.price, ))
    con.commit() #입력,삭제, 수정에 꼭!
    cursor.close()
    con.close()

#읽기 함수(한개값)
def read(code):
    con=sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from product where code=?"
    cursor.execute(sql,(code, ))
    row = cursor.fetchone()
    cursor.close()
    con.close()
    return row

#찾기 함수
def search(name):
    con=sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "select * from product where name like ?"
    cursor.execute(sql, (f'%{name}%',))
    rows = cursor.fetchall()
    cursor.close()
    con.close()
    return rows

#삭제 함수
def delete(code):
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "delete from product where code=?"
    cursor.execute(sql,(code,))
    con.commit()
    cursor.close()
    con.close()

#수정 함수
def update(p): #전부 받아야하니 p로 객체
    con = sqlite3.connect(db_name)
    cursor = con.cursor()
    sql = "update product set name=?, price=? where code=?"
    cursor.execute(sql, (p.name, p.price, p.code,))
    con.commit()
    cursor.close()
    con.close()



##
#update 테스트 함수
def update_test():
    code = int(input("수정코드>"))
    row = read(code)
    p = rowPrint(row) #배열-프로덕트로/리턴한 프로덕트값=p
    if p != None:
        name = input(f"상품명:{p.name}>")
        if name !="": p.name = name
        price = input(f"상품가:{p.price:,}>")
        if price !="": p.price = int(price) #정수로 변경
        update(p)
        print("수정완료!")

#delete 테스트 함수
def delete_test():
    code = int(input("삭제코드>"))
    row = read(code) #삭제할 데이터 불러오기
    if row == None:
        print("삭제할 상품 코드가 없습니다.")
    else:
        rowPrint(row)
        delete(code)
        list_test(1)


#search 테스트 함수
def search_test():
    while True:
        name = input("상품명>")
        if name =="": break
        rows = search(name)
        for row in rows:
            rowPrint(row)

#read 테스트 함수
def read_test():
    code = int(input("상품코드>"))
    row = read(code) #로우 리드결과
    if row == None:
        print("상품 코드가 없습니다.")
    else:
        rowPrint(row)

#insert 테스트 함수
def insert_test(p):
    p = Product()
    p.name = input("상품명>")
    p.price = int(input("상품가>"))
    insert(p)

#리스트 옵션체크 테스트 함수
def list_test(type):
    rows = list(type)
    for row in rows:
        rowPrint(row)

#테스트
if __name__=='__main__':
    update_test()
        
        # #rowPrint 테스트
        # rows = list(1)
        # for row in rows:
        #     rowPrint(row)
        
        # #delete_test 테스트
        # delete_test()

        # #search_test 테스트
        # search_test()

        # #read_test 테스트
        # while True:
        #     read_test()

        # #상품 입력 테스트
        # p = Product()
        # insert_test(p)
        # list_test(1)

        # #리스트 테스트
        # list_test(1)