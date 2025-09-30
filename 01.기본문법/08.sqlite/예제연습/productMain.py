from function import *
from productDB import *

while True:
    menuPrint("상품관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print("프로그램을 종료합니다.")
        break

    elif menu == "1": #입력
        p = ProcessLookupError()
        p.name = input("상품명>")
        if p.name=="": continue
        p.price = inputNum("상품가격>")
        if p.price =="": p.price = 0
        insert(p)
        print("상품 등록 완료!")

    elif menu == "2": #검색 ## 해당상품 없음 출력이 안됨
        while True:
            value = input("검색어>")
            if value =="": 
                print("메뉴로 돌아갑니다.")
                break
            rows = search(value)
            for row in rows:
                rowPrint2(row)
    
    elif menu == "3": #목록
        while True:
            type = inputNum("1.코드순|2.상품명순|3.최저가|4.최고가>")
            if type == "": break
            rows = list(type)
            for row in rows:
                rowPrint(row)
    
    elif menu == "4": #삭제
        code = inputNum("상품코드>")
        if code=="": 
            print("메뉴로 돌아갑니다.")
            continue
        row = read(code)
        p = rowPrint(row)
        if p !=None:
            sel = input("삭제하시겠습니까?(Y/N)>")
            if sel =="Y" or sel =="y":
                delete(code)
                print("상품 삭제 완료!")
            else:
                print("삭제가 취소되어 메뉴로 돌아갑니다.")
                continue
    
    elif menu == "5": #수정
        code = inputNum("상품코드>")
        if code=="": 
            print("메뉴로 돌아갑니다.")
            continue
        row = read(code)
        p = rowPrint(row)
        if p !=None:
            name = input(f"상품명:{p.name}>")
            if name !="": p.name = name
            price = input(f"상품가격:{p.price:,}원>")
            if price !="": p.price = int(price)   

            sel = input("수정하시겠습니까?(Y/N)>")
            if sel =="Y" or sel =="y":
                update(p)
                print("상품 수정 완료!")
            else:
                print("수정이 취소되어 메뉴로 돌아갑니다.")
                continue

    else:
        print("0~5 메뉴를 선택하세요!")
        continue