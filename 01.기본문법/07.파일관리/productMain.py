from function import *
from productfile import *

def newCode(): #새로운 상품번 리턴함수
    list = fileRead()
    result = sorted(list, key=lambda p:p.code, reverse=True)
    if len(list)==0:
        return 1
    else:
        p = result[0]
        return p.code+1

while True:
    menuPrint("상품관리")
    menu = input("메뉴선택>")
    if menu =="0": #종료
        print("프로그램을 종료합니다.")
        break

    elif menu == "1": #입력
        p= Product()
        p.code = newCode()
        print(f"상품번>{p.code}")
        if p.code == "": 
            print("메뉴로 돌아갑니다.")
            continue
        p.name = input("상품명>")
        if p.name == "": 
            print("메뉴로 돌아갑니다.")
            continue
        p.price = input("상품가격>")
        if p.price == "":
            print("메뉴로 돌아갑니다.")
            continue
        fileAppend(p)
        print("등록성공!")

    elif menu == "2": #검색
        while True:
            value = input("상품명>")
            if value == "": 
                print("메뉴로 돌아갑니다.")
                break
            list = fileRead()
            result = [p for p in list if p.name.find(value)!=-1]
            if len(result) ==0:
                print("검색내용이 없습니다.")
                continue
            for p in result:
                p.print()

    elif menu == "3": #목록
        while True:
            sort = inputNum("1.코드순|2.이름순|3.최저가|4.최고가>")
            if sort == "": 
                print("메뉴로 돌아갑니다.")
                break
            list = fileRead()
            result = []
            if sort == 1:result = sorted(list, key =lambda p:p.code) #람다(한줄함수 단일값, 기본 오름차순)
            if sort == 2:result = sorted(list, key =lambda p:p.name)
            if sort == 3:result = sorted(list, key =lambda p:p.price)
            if sort == 4:result = sorted(list, key =lambda p:p.price, reverse=True) #역순
            print()
            for p in result:
                p.print()
        # for p in list:
        #     p.print()

    elif menu == "4": #삭제
        code = inputNum("삭제상품번>")
        list = fileRead()
        result = [p for p in list if p.code == code]
        if len(result) == 0:
            print("삭제할 번호가 없습니다.")
            continue
        p = result[0]
        p.print()
        sel = input("삭제하시겠습니까?(Y/N)>")
        if sel == "Y" or sel =="y":
            result = [p for p in list if p.code!=code]
            fileWrite(result)
            print("삭제성공!")
        else:
            print("상품 삭제가 취소되었습니다.")

    elif menu == "5": #수정
        code = inputNum("수정상품번>")
        if code == "":
            print("상품 수정이 취소되었습니다.")
            continue
        list = fileRead()
        result = [p for p in list if p.code == code]
        if len(result) == 0:
            print("수정할 번호가 없습니다.")
            continue
        p = result[0]
        name = input(f"이름:{p.name}>")
        if name!="": p.name = name
        price = inputNum(f"상품가격:{p.price}>") #숫자입력시 명령어 주의
        if price !="": p.price = price
        sel = input("수정하시겠습니까?(Y/N)>")
        if sel == "Y" or sel =="y":
            p.print()
            fileWrite(list)
            print("수정성공!")
        else:
            print("상품 수정이 취소되었습니다.")

    else:
        print("0~5 메뉴를 고르세요!")                