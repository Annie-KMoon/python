from student import Student

class Score(Student): #Score는 Student를 상속, 학생->스코어(속성상속)
    def __init__(self): #성적 객체 자동생성자 / enter, 자동으로 생성자 생성 (super()=Student)
        super().__init__()
        self.kor = 0
        self.eng = 0
        self.mat = 0

    def info_print(self): #성적 객체의 정보 출력 매서드(함수)
        super().info_print()
        print(f"국어:{self.kor},영어:{self.eng},수학:{self.mat}")

    def result(self): #결과 구분 매서드
        avg = (self.kor+self.eng+self.mat)/3
        if avg < 70:
            return "FAIL"
        else:
            return "PASS"

    def dict(self): #딕셔너리로 변환하는 메서드(함수)
        return {'no':self.no, 'name':self.name, 
                'kor':self.kor, 'eng':self.eng, 'mat':self.mat,
                'avg':((self.kor+self.eng+self.mat)/3), 
                'result':self.result()}
    

if __name__=='__main__':
    s = Score() #클래스네임() > s. 하면 속성 표기
    s.no = '01'
    s.name = '홍길동'
    s.kor = 90
    s.eng = 90
    s.mat =80
    print(s.dict())
