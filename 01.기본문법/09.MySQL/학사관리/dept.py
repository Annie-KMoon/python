import os
from DB import *

def menuDept():

    while True:
        os.system('cls')
        print('*********학과관리*********')
        print('-------------------------')
        print("1.등록|2.목록|3.수정|0.종료")
        print('-------------------------')
        menu = input("메뉴선택>")
        if menu == "0":
            print("학과관리를 종료합니다.")
            input("아무 키나 누르세요.")
            break

        elif menu == "1": #등록
            try:
                dname = input("학과이름>")
                if dname =="":
                    print("등록을 종료하고 학과관리로 돌아갑니다.")
                    input("아무 키나 누르세요.")
                    continue
                insertDept(dname)
            except Exception as err:
                print("학과등록오류:",err)

        elif menu == "2": #목록
            try:
                depts = listDept()
                for dept in depts:
                    dept.print() #dept에서 프린트함수생성
                input("메뉴로 돌아가려면 아무 키나 누르세요.")
            except Exception as err:
                print("학과목록오류:",err)


        elif menu == "3": #수정
            try:
                dcode = inputCode("수정할 코드>",5)
                if dcode == "":
                    print("수정을 종료하고 학사관리로 돌아갑니다.")
                    input("메뉴로 돌아가려면 아무 키나 누르세요.")
                    continue
                dept = readDept(dcode)
                dname = input(f'수정할 학과이름:{dept.dname}>')
                if dname!="":
                    dept.dname = dname
                updateDept(dept)
                input("메뉴로 돌아가려면 아무 키나 누르세요.")
            except Exception as err:
                print("학과목록오류:",err)

        else:
            print("0~3의 메뉴를 선택하세요.")
            input("메뉴로 돌아가려면 아무 키나 누르세요.")
            continue