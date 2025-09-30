import pymysql

#커넥션 설정:
#내PC서버 사용 'localhost'or ip주소 작성 가능'유저, 비번, 디비, 한글사용,커서클래스 설정
con = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='haksa',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor) #dict커서사용
cur = con.cursor()

#클래스설정
class Dept:
    def __init__(self):
        self.dcode = 0
        self.dname = ""

    def print(self):
        print(f'학과코드:{self.dcode}, 학과이름:{self.dname}')

class Student(Dept):
    def __init__(self):
        super().__init__()
        self.id = ""
        self.name = ""
        self.code = 0

    def print(self):
        print(f"학번:{self.id}, 이름:{self.name}, 학과:{self.dname}({self.code})")
        print("-"*70)


#메뉴별 함수 설정
def list(key):
    try:
        keys=['id','name','dname']
        sql = f'select * from vstudent order by {keys[key-1]}' #괄호주의
        cur.execute(sql)
        rows = cur.fetchall()
        list =[]
        for row in rows:
            stu = Student()
            stu.id = row['id'] #dict키 사용, row번호외 키네임 사용가능
            stu.name = row['name']
            stu.dname = row['dname']
            stu.code = row['code']
            list.append(stu)
        return list
    except Exception as err:
        print("학생목록오류:",err)

#검색함수
def search(value):
    try:
        sql = 'select * from vstudent where id like%s or name like%s or dname like%s' #mySQL= ?대신 %s사용
        value = f'%{value}%'
        cur.execute(sql, (value, value, value,))
        rows =cur.fetchall()
        if rows!=None:
            list=[]
            for row in rows:
                stu = Student()
                stu.id = row['id']
                stu.name = row['name']
                stu.code = row['code']
                stu.dname = row['dname']
                list.append(stu)
            return list

    except Exception as err:
        print("학생검색오류:",err)

#학과목록 출력 함수
def listDept():
    try:
        sql = 'select * from dept'
        cur.execute(sql)
        rows = cur.fetchall()
        list = []
        for row in rows:
            dept = Dept()
            dept.dcode = row['dcode']
            dept.dname = row['dname']
            list.append(dept)
        return list
    
    except Exception as err:
        print("학과목록출력오류:",err)

#학과코드 입력 함수
def inputCode(title, menu): #menu1-입력, menu5-수정
    try:
        depts = listDept()
        print('-'*50)
        for dept in depts:
            print(f'{dept.dcode}.{dept.dname}',end="|")
        print()
        print('-'*50)
        codes = [dept.dcode for dept in depts]
        while True:
            code = input(title)
            if code == "" and menu == 1: #입력
                print("학과코드를 꼭 입력하세요.")
            elif code == "" and menu == 5: #수정
                return code
            elif not code.isnumeric():
                print("학과코드는 숫자로 입력하세요.")
            elif codes.count(int(code))==0:
                print(f'{codes}의 코드번호를 입력하세요!')                 
                # print(f'{min(codes)}~{max(codes)}의 코드번호를 입력하세요!') 
                print
            else:
                return int(code) #최종int값
    except Exception as err:
        print("학과코드입력오류:",err)     

#New Id 함수
def newID():
    try:
        sql = 'select convert(max(id)+1, char(4)) as new_id from student'
        cur.execute(sql)
        row =cur.fetchone()
        return row['new_id']
    except Exception as err:
        print("신규학번오류:",err)

#입력
def insert(stu): #정보를 받을 object 설정-stu
    try:
        sql = 'insert into student(id, name, code) values(%s,%s,%s)'
        cur.execute(sql, (stu.id, stu.name, stu.code,))
        con.commit()
        print("학생정보등록성공!")

    except Exception as err:
        print("학생정보등록오류:",err)

#학과입력함수 - 각 테이블 모듈 별도로 파일 생성, 이름 중복 안되게 주의
def insertDept(dname):
    sql = 'insert into dept(dname) values(%s)'
    cur.execute(sql,(dname,))
    con.commit()
    print("학과등록 완료!")

# 학과리드함수 - 각 테이블 모듈 별도로 파일 생성, 이름 중복 안되게 주의
def readDept(dcode):
    sql = 'select * from dept where dcode=%s'
    cur.execute(sql,(dcode,))
    row = cur.fetchone()
    if row !=None: #값이 있을때만 리턴
        d = Dept() #객체만들어서 로우값
        d.dcode = row ['dcode']
        d.dname = row['dname']
        return d
#학과수정함수
def updateDept(dept):
    sql = 'update dept set dname=%s where dcode=%s'
    cur.execute(sql, (dept.dname, dept.dcode))
    con.commit()
    print("학과정보수정성공!")

#읽기(수정,삭제를 위한 읽기함수)
def read(id):
    try:
        sql = "select * from vstudent where id =%s"
        cur.execute(sql, (id,))
        row = cur.fetchone()
        if row !=None: #값이 있을때만 리턴
            stu = Student() #객체만들어서 로우값
            stu.id = row ['id']
            stu.name = row['name']
            stu.code = row['code']
            stu.dname = row['dname']
            return stu
    except Exception as err:
        print("학생정보읽기오류:", err)

#삭제
def delete(id):
    try:
        sql = "delete from student where id =%s"
        cur.execute(sql, (id,))
        con.commit()
        print("학생정보삭제성공!")

    except Exception as err:
        print("학생정보삭제오류:",err)

#수정
def update(stu): #학생 전체정보 받기
    try:
        sql = 'update student set name=%s, code=%s where id=%s'
        cur.execute(sql, (stu.name, stu.code, stu.id,))
        con.commit()
        print("학생정보수정성공!")

    except Exception as err:
        print("학생정보수정오류:", err)


#테스트#
if __name__=='__main__':
    pass

    # #read test
    # id = input("학번>")
    # stu = read(id)
    # if stu == None:
    #     print("학생정보가 없습니다.")
    # else:
    #     stu.print()

    # #input code test
    # code = inputCode('학과코드>',1)
    # print('입력한 학과코드:',code)

    # #입력 테스트 - err
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

    # #학과읽기 테스트
    # stu = read('2501')
    # if stu ==None:
    #     print("학생 정보가 없습니다.")
    # else:
    #     stu.print()

    # #입력테스트
    # code = inputDept(f"학과코드>",5)
    # print("입력한 학과코드:",code)

    # #listDept 테스트
    # depts = listDept()
    # for dept in depts:
    #     print(f'{dept.dcode}.{dept.dname}',end = '|')
    # print()
    # print('-'*50)
    # while True:

    # #newID 테스트
    # print(f"새로운 학번: {newID()}")


    # #검색 테스트
    # while True:
    #     value = input("검색어>")
    #     if value == "": break
    #     else:
    #         students = search(value)
    #         if len(students) == 0:
    #             print("검색하신 학생 정보가 없습니다.")
    #         else:
    #         # if students !=None:
    #             for stu in students:
    #                 stu.print()


    # students = list()>>키값설정필요
    # for stu in students:
    #     stu.print()

    # rows = list()
    # print(len(rows))