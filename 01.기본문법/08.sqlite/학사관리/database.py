from function import *
import os, sqlite3
path = os.path.dirname(os.path.realpath(__file__))
# print(path)
db_name = path + '/haksa.db'

#전체로 커넥,커서 오픈
con = sqlite3.connect(db_name)
cur = con.cursor()


#클래스 
class Dept:
    def __init__(self): #Dept 객체 생성자
        self.code = 0
        self.dname = ''
        
    def print(self):
        print(f"{self.code}.{self.name}",end="|")

class Student(Dept): #S.는 D 상속
    def __init__(self):
        super().__init__()
        self.id = ''
        self.name =''
        self.dept = 0 #생략가능
    
    #학생정보 출력 함수
    def print(self):
        print(f"학번:{self.id},이름:{self.name}, 학과:{self.dname}({self.dept})")

#목록 출력 함수
def list(): #전체목록
    try:
        sql = 'select * from vstudent'
        cur.execute(sql)
        rows = cur.fetchall() #리스트안에 객체를 넣어서 출력>프론트에서 간단하게=클래스사용
        list=[] #리스트 설정
        for row in rows:
            stu = Student() #클래스로 만든 객체로 저장
            stu.id = row[0] #idx 넘버 SQL에서 확인, sql문에 순서대로 작성OK
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu) #리스트에 객체 in
        return list #여러 학생데이터가 리스트로 in / juso에서는 row로 리턴
    except Exception as err:
        print("목록 오류:", err)
    # finally: #try/except 결과마다
    #     pass


#학과목록 출력 함수
def listDept(): 
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.code = row[0]
            dept.name = row[1]
            list.append(dept)
        return list 
    except Exception as err:
        print("학과목록오류:", err)
    finally: #try/except 결과마다
        pass

#검색 함수
def search(value):
    try:
        sql  ='select * from vstudent where name like ? or id like ? or dname like ?'
        # sql += ' and (name like ? or id like ? or dname like?) ' #sql 만족 조건 +=(추가조건)연산순위 묶음 주의, eq-완전만족/ view 미생성시 두개테이블 전부 기입
        value = f'%{value}%' #부분일치 검색
        cur.execute(sql, (value, value, value,)) #끝에 ,생략해도됨
        rows = cur.fetchall() #검색값 전부 패치
        list=[] #리스트 설정
        for row in rows:
            stu = Student() #클래스로 만든 객체로 저장
            stu.id = row[0] #idx 넘버 SQL에서 확인, sql문에 순서대로 작성OK
            stu.dept = row[1]
            stu.name = row[2]
            stu.dname = row[3]
            list.append(stu) #리스트에 객체 in
        return list #여러 학생데이터가 리스트로 in / juso에서는 row로 리턴
    except Exception as err:
        print("검색 오류:", err)
    # finally: #try/except 결과마다
    #     pass

#id번호 생성 함수
def newID():
    try:
        sql = 'select max(id)+1 from student'
        cur.execute(sql)
        row = cur.fetchone()
        new_id = row[0]
        return new_id
    except Exception as err:
        print("코드생성:",err)
    finally:
        pass
        # cur.close()
        # con.close()

#등록함수
def insert(stu): #stu-object, 
    try:
        sql = 'insert into student(id, name, dept) values(?,?,?)'
        cur.execute(sql, (stu.id, stu.name, stu.dept,))
        con.commit()
    except Exception as err:
        print("입력오류:",err)
    finally:
        pass
        # cur.close()
        # con.close()

#학과입력 함수 - 다양한 메뉴에 쓰도록 type 설정하여 정리
def inputDept(title, type):
    depts = listDept() #기존 학과코드 출력
    for dept in depts:
        print(f'{dept.code}.{dept.name}',end='|')
    print() #줄바꿈
    codes = [dept.code for dept in depts]
    while True: #학과입력
        code=input(title)
        if code == "" and type ==5:
            return ""
        elif code == "" and type ==1:
            print("학과코드는 반드시 입력하세요!")
        elif not code.isnumeric():
            print("학과코드는 숫자로 입력하세요!")
            continue
        elif codes.count(int(code)) ==0: #count 함수 사용
            print(f'{min(codes)}~{max(codes)}의 숫자를 입력하세요!')
        else:
            return int(code)

#읽기 함수
def read(id):
    try:
        sql = "select id, name, dept, dname from vstudent where id =?"
        cur.execute(sql, (id,))
        row = cur.fetchone()
        if row !=None:
            stu = Student()
            stu.id = id
            stu.name = row[1]
            stu.dept = row[2]
            stu.dname = row[3]
            return stu
    except Exception as err:
        print("학번 읽기 오류:", err)

#삭제 함수
def delete(id):
    try:
        sql = "delete from student where id =?"
        cur.execute(sql, (id,))
        con.commit()

    except Exception as err:
        print("학생 정보 삭제 오류:",err)


#수정함수
def update(stu): #학생 전체정보 받기
    try:
        sql = "update student set name=?, dept=? where id=?"
        cur.execute(sql, (stu.name, stu.dept, stu.id,))
        con.commit()

    except Exception as err:
        print("학생 정보 수정 오류", err)



#테스트#
if __name__ == '__main__':
    pass

    # #학과입력테스트
    # code = inputDept()

    #입력 테스트
    # stu = Student()
    # stu.id = newID()
    # print(f"학번:{stu.id}")
    # stu.name = input("이름>")
    # if stu.name == "":
    #     print("이름을 반드시 입력하세요!")
    # else:
    #     stu.dept = int(input("학과코드>"))
    # insert(stu)
    # print("데이터 입력 성공!")

    #newID 테스트
    # print(newID())

    #검색 테스트
    # value = input("검색어>")
    # students = search(value)
    # if students !=None:
    #     for stu in students:
    #         stu.print()

    #출력테스트
    # students = list()
    # # if students ==None:
    # #     print("데이터가 없습니다.")
    # if students !=None:
    #     for stu in students:
    #         stu.print()

    # #학과출력테스트
    # depts = listDept()
    # if depts !=None:
    #     for d in depts:
    #         d.print()

    # #입력테스트
    # code = inputDept(f"학과코드>")
    # print("입력한 학과코드:",code)

    # #학과읽기 테스트
    # stu = read('2501')
    # if stu ==None:
    #     print("학생 정보가 없습니다.")
    # else:
    #     stu.print()
