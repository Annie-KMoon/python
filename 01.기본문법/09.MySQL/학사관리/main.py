from function import *
from DB import *
from dept import *
import os

while True:
    os.system('cls') #os시스템, 클로즈
    menuPrint("학사관리")
    menu = input("메뉴선택>")
    if menu == "0":
        cur.close() #함수화 가능?
        con.close()
        print("프로그램을 종료합니다.")
        input("아무 키나 누르세요.")
        break
    elif menu == "1": #입력
        stu = Student() #입력할 객체 생성
        stu.id = newID()
        print(f'신규ID>{stu.id}')
        while True:
            stu.name = input("학생이름>")
            if stu.name == "":
                print("학생 이름을 꼭 입력하세요.")
                continue
            else:
                break
        stu.code = inputCode("학과코드>",1) #code 명칭 체크
        stu.print()
        sel = input("입력 하시겠습니까?(Y/N)")
        if sel == "Y" or sel == "y":
            insert(stu)
            input("아무 키나 누르세요.")
        else:
            print("입력을 취소하고 메뉴로 돌아갑니다.")
            input("아무 키나 누르세요.")
            continue

    elif menu == "2": #검색
        while True:
            value = input("검색어>")
            if value == "": 
                input("메뉴로 돌아가려면 아무 키나 누르세요.")
                break
            students = search(value)
            if len(students) == 0:
                print("검색하신 학생 정보가 없습니다.")
            else:
                for stu in students:
                    stu.print()

    elif menu == "3": #목록
        while True:
            key = inputNum("1.ID순|2.이름순|3.학과순>")
            if key == "":
                print("메뉴로 돌아갑니다.")
                input("아무 키나 누르세요.")
                break
            elif key <1 or key>3:
                print("1~3의 숫자를 입력하세요!")
                continue
            else:
                students = list(key)
                for stu in students:
                    stu.print()
                print(f"총 {len(students)}명의 학생이 존재합니다.")

    elif menu == "4": #삭제
        id = input("삭제할 ID>")
        if id == "":
            print("삭제를 종료하고 메뉴로 돌아갑니다.")
            input("아무 키나 누르세요.")
            continue
        stu = read(id)
        if stu ==None:
            print("삭제할 학생 정보가 없습니다.")
            input("아무 키나 누르세요.")
        else:
            stu.print()
            sel = input("삭제하시겠습니까?(Y/N)>")
            if sel == "Y" or sel =="y":
                delete(id)
                input("아무 키나 누르세요.")
            else:
                print("삭제를 종료하고 메뉴로 돌아갑니다.")
                input("아무 키나 누르세요.")
                continue

    elif menu == "5": #수정
        id = input("수정할 ID>")
        if id == "":
            print("수정을 종료하고 메뉴로 돌아갑니다.")
            input("아무 키나 누르세요.")
            continue
        stu = read(id)
        if stu ==None:
            print("수정할 학생 정보가 없습니다.")
            input("아무 키나 누르세요.")
        else:
            stu.print()
            sel = input("수정하시겠습니까?(Y/N)>")
            if sel == "Y" or sel =="y":
                name = input(f'학생이름:{stu.name}>')
                if name !="":
                    stu.name = name
                code = inputCode(f'학과코드:{stu.code}>',5)
                if code !="":
                    stu.code = code
                update(stu)
                input("아무 키나 누르세요.")
            else:
                print("수정을 종료하고 메뉴로 돌아갑니다.")
                input("아무 키나 누르세요.")
                continue

    elif menu == "6": #학과관리
        menuDept()            #별도 모듈로 생성 관리

    else:
        print("0~6의 메뉴를 선택하세요!")
        continue