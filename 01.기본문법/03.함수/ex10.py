from function2 import * #*는 함수 전부 사용

sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

while True:
    menuPrint("상품관리")
    menu  = input("메뉴 선택>")
    if menu == "0": #종료
        print("프로그램을 종료합니다.")
        break
    elif menu == "1": #입력
        new_code = newCode(sale)
        print(f"상품코드>{new_code}")
        new_name = input("상품이름>")
        if new_name == "":
            continue
        new_price = inputNum("상품가격(만원)>")
        if new_price == "":
            continue
        if new_price == "": new_price=0
        new_qnt = inputNum("판매수량>")
        if new_price == "": new_qnt=0
        sale.append({'code':new_code, 'name':new_name, 'price':new_price, 'qnt':new_qnt})
        print("등록 완료")

    elif menu == "2": #검색
        code = inputNum("검색코드>")
        idx = search(sale, code)
        if idx == None:
            print(f"{code}번 상품이 없습니다.")
        else:
            s = sale[idx]
            print(f"상품이름:{s['name']}")
            print(f"상품가격:{s['price']:,}만원")
            print(f"판매수량:{s['qnt']:,}개")
            print(f"총매출액:{s['price']*s['qnt']:,}만원")

    elif menu == "3": #목록
        for s in sale:
            itemPrint(s)

    elif menu == "4": #삭제
        code = inputNum("삭제코드>")
        if code == "": 
            print("메뉴로 다시 돌아갑니다.")
            continue
        idx = search(sale, code)
        if idx==None:
            print(f"{code}번 상품이 없습니다.")
        else:
            s = sale[idx]
            print(s)
            sel = input("삭제하시겠습니까?(Y/N)")
            if sel == "Y" or sel == "y":
                sale.pop(idx)
                print("삭제 완료")
            else:
                print("메뉴로 다시 돌아갑니다.")
                continue

    elif menu == "5": #수정
        code = inputNum("수정번호>")
        if code =="": 
            print("메뉴로 다시 돌아갑니다.")
            continue
        idx = search(sale,code)
        if idx == None:
            print(f"{code}번 상품이 없습니다.")
            continue
        s= sale[idx]
        new_name = input(f"상품이름:{s['name']}>")
        if new_name == "": new_name = s['name']
        new_price = inputNum(f"상품가격:{s['price']:,}만원>")
        if new_price == "": new_price = s['price']
        new_qnt = inputNum(f"판매수량:{s['qnt']:,}개>")
        if new_qnt == "": new_qnt = s['qnt']
        # print("수정사항:",new_name, new_price, new_qnt)
        sel = input("수정하시겠습니까?(Y/N)")
        if sel == "Y" or sel == "y":
            sale[idx]={'code':code, 'name':new_name, 'price':new_price, 'qnt':new_qnt}
            print("수정완료!")
        else:
            print("메뉴로 다시 돌아갑니다.")
            continue
    else:
        print("0~5를 입력하세요.")         