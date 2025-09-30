class Student:
    def __init__(self): #객체생성자
        self.no = '' #객체의 속성
        self.name = ''
        self.dept = '컴정과' #고정값이 있는 경우 def에 작성
        self.birthday = '00-10-04'

    def info_print(self): #학생 속성을 출력하는 매서드(함수)
        print(f"학번:{self.no}", end=",")
        print(f"성명:{self.name}", end=",")
        print(f"학과:{self.dept}", end=",")
        print(f"생일:{self.birthday}")      

    def info(self): #학생정보 dict 생성 매서드(함수)
        return {'no':self.no, 'name':self.name, 'dept':self.dept, 'birthday':self.birthday} 

if __name__=='__main__':
    s = Student() #클래스네임() > s. 하면 속성 표기
    s.no = '01'
    s.name = '홍길동'
    s.birthday = '02-12-17'
    print(s.info_print())
    # s.info_print() #s. 함수 표기
    # print(s.info())