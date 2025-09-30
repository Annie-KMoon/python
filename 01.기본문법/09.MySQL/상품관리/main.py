#상품관리 main

import os
from DB import *
from productDB import *
from sub import*

while True:
    os.system('cls') #os시스템, 클로즈
    print('====================================')
    print('             상품관리                ')
    print('====================================')
    print('[1] 상품등록')
    print('[2] 상품검색')
    print('[3] 상품목록')
    print('[4] 상품정보수정')
    print('[5] 매출관리')
    print('[0] 프로그램종료')
    menu = input("메뉴선택>")
    if menu == "0":
        cur.close()
        con.close()
        input("프로그램을 종료합니다. 종료하기 위해 아무 키나 누르세요.")
        break
    elif menu =="1": #상품등록 / 코드생성을 위한inputcode등 사용
        code = inputCode("신규코드>")
        if code == "":
            input("입력을 취소하고 메뉴로 돌아갑니다. 아무 키나 누르세요.")
            continue
        pro = read(code)
        if pro !=None:
            pro.print()
            print("이미 등록된 상품입니다!")
            input("메뉴로 돌아가려면 아무 키나 누르세요.")
        else:
            pro = Product()
            pro.code=code
            pro.name = input("신규상품명>") #공란 입력시 수정에서 수정하는걸로
            pro.price = inputPrice("상품소비자가")
            if pro.price == "": pro.price=0
            pro.print()
            sel = input("입력 하시겠습니까?(Y/N)")
            if sel == "Y" or sel == "y":
                insert(pro)
                input("메뉴로 돌아가려면 아무 키나 누르세요.")
            else:
                input("입력을 취소하고 메뉴로 돌아갑니다. 아무 키나 누르세요.")

    elif menu =="2": #상품검색
        while True:
            value = input("검색어>")
            if value == "": 
                print("검색을 종료합니다.")
                break
            products = search(value)
            if len(products)==0:
                print("검색한 상품이 없습니다.")
            else:
                for product in products:
                    product.print()
        input("메뉴로 돌아가려면 아무 키나 누르세요.")
    
    elif menu =="3": #상품목록
        products = product_list()
        for product in products:
             product.print()
        input("메뉴로 돌아가려면 아무 키나 누르세요.")

    elif menu =="4": #상품정보수정
        code = inputCode("수정할 상품코드>")
        product=read(code)
        if code == "":
            input("수정을 취소하고 메뉴로 돌아갑니다. 아무 키나 누르세요.")
        elif product == None:
            input("입력한 코드는 등록되지 않은 상품입니다..")
            input("수정을 취소하고 메뉴로 돌아갑니다. 아무 키나 누르세요.")
        else:
            name = input(f'상품명:{product.name}>')
            if name !="": product.name =name
            price = inputPrice(f'상품소비자가:{product.price:,}원>')
            if price !="": product.price = price
            product.print()
            sel = input("수정 하시겠습니까?(Y/N)")
            if sel == "Y" or sel == "y":
                update(product)
                input("메뉴로 돌아가려면 아무 키나 누르세요.")
            else:
                input("수정을 취소하고 메뉴로 돌아갑니다. 아무 키나 누르세요.")

    elif menu =="5": #매출관리
        saleMenu()
        pass

    else:
        print("[0]~[5]의 메뉴를 선택하세요!")
        input("메뉴로 돌아가려면 아무 키나 누르세요.")
        continue






