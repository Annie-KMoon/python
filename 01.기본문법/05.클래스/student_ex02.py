from student import Student #from 모듈 import 클래스

students = [
    {'no':'01', 'name':'홍길동', 'dept':'컴퓨터공학과','birthday': '00-10-04'},
    {'no':'02', 'name':'심청이', 'dept':'전기전자공학과','birthday': '02-12-29'}    
]
while True:
    print('---------------------')
    print('|1.등록|2.목록|3.삭제|0.종료')
    print('---------------------')
    menu = input("메뉴 선택>")
    if menu == "0": #종료
        print("프로그램을 종료합니다.")
        break

    elif menu == "1":#등록
        s = Student() #객체등록
        s.no = input("번호>")
        s.name = input("이름>")
        s.dept = input("학과>")
        s.birthday = input("생일>")
        students.append(s.info())

    elif menu == "2":#목록
        for s in students:
            stu = Student()
            stu.no = s['no']
            stu.name = s['name']
            stu.dept = s['dept']
            stu.birthday = s['birthday']
            stu.info_print()
            
    elif menu == "3":#삭제
        no = input("삭제번호>")
        for index, s in enumerate(students):
            if no == s['no']:
                students.pop(index)
                print("삭제완료")
                break #찾고 삭제 완료,종료


                        
    else:
        print("0~2번 메뉴를 누르시오.")

