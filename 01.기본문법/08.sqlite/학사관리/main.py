from function import *
from database import *

while True:
    menuPrint("학생관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print("프로그램을 종료합니다.")
        cur.close() #함수화 가능?
        con.close()
        break

    elif menu =="1": #입력
        stu = Student()
        stu.id = newID()
        print(f"학번:{stu.id}")
        while True:
            stu.name = input("이름>")
            if stu.name =="":
                print("이름을 반드시 입력하세요.")
                continue
            else:
                break
        stu.dept = inputDept("학과코드>",1)
        sel = input("입력을 하시겠습니까?(Y/N)")
        if sel =="y" or sel =="Y":
            stu.print
            insert(stu)
            print("학생 정보 등록 성공!")
        else:
            print("입력을 취소하고 메뉴로 돌아갑니다.")
            continue

    elif menu =="2": #검색
        while True:
            value = input("검색어>")
            if value =="": 
                print("메뉴로 돌아갑니다.")
                break
            students = search(value)
            if students==None:
                print("검색결과가 없습니다.")
                continue
            for stu in students:
                stu.print()
            print(f"총 {len(students)}명의 학생이 존재합니다.\n")

    elif menu =="3": #목록
        students = list()
        # if students !=None:
        for stu in students:
            stu.print()
        print(f"총 {len(students)}명의 학생이 존재합니다.")

    elif menu =="4": #삭제
        id = input("삭제할 학번>")
        if id == "":
            print("삭제를 종료하고 메뉴로 돌아갑니다.")
            continue
        stu = read(id)
        if stu ==None:
            print("삭제할 학생 정보가 없습니다.")
        else:
            stu.print()
            sel = input("삭제하시겠습니까?(Y/N)>")
            if sel == "y" or sel =="Y":
                delete(id)
                print("학생정보 삭제 성공!")
            else:
                print("삭제를 종료하고 메뉴로 돌아갑니다.")
                continue

    elif menu =="5": #수정
        id = input("수정할 학번>")
        if id == "":
            print("수정 종료하고 메뉴로 돌아갑니다.")
            continue
        stu = read(id)
        if stu ==None:
            print("수정할 학생 정보가 없습니다.")
            continue
        else:
            stu.print()
            sel = input("수정하시겠습니까?(Y/N)>")
            if sel == "y" or sel =="Y":
                name = input(f"이름:{stu.name}>")
                if name !="":
                    stu.name = name
                dept = inputDept(f"학과코드:{stu.dept}>",5)
                if dept!="":
                    stu.dept = dept
                update(stu)
                print("학생정보 수정 성공!")
            else:
                print("수정을 종료하고 메뉴로 돌아갑니다.")
                continue

    else:
        print("0~5의 메뉴를 선택하세요!")