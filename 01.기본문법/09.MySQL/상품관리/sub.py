#매출관리 DB
import os
from saleDB import*
from productDB import *
from classes import*

def saleMenu():
    while True:
        os.system('cls') 
        print('------------------------------------')
        print('             매출관리                ')
        print('------------------------------------')
        print('(1) 매출등록')
        print('(2) 매출검색')
        print('(3) 매출목록')
        print('(4) 매출정보수정')
        print('(5) 매출정보삭제')
        print('(0) 프로그램종료')
        
        menu = input("메뉴선택>")
        if menu =="0": #종료
            input("매출관리를 종료하기 위해 아무 키나 누르세요.")
            break
        elif menu =="1": #매출등록
            code = inputCode("매출등록코드>")
            pro = read(code)
            if pro == None:
                print("등록된 상품이 없습니다.")
            else:
                pro.print()
                sale = Sale()
                sale.code = code
                price = inputPrice(f"상품판매가(소비자가:{pro.price:,}원)>")
                if price!="": 
                    sale.price = pro.price
                # elif price !=None: # 수정해보세용
                    sale.price = price
                qnt = inputNum(f"판매수량>")
                if qnt=="": return 0
                sale.qnt = qnt
                print(f'상품코드:{sale.code},판매가:{sale.price:,}원, 판매수량:{sale.qnt}개')
                sel = input("입력 하시겠습니까?(Y/N)")
                if sel == "Y" or sel == "y":
                    sale_insert(sale)
                    con.commit()
                    input("메뉴로 돌아가려면 아무 키나 누르세요.")
                else:
                    input("입력을 취소하고 메뉴로 돌아갑니다. 아무 키나 누르세요.")
            pass
        elif menu =="2":#매출검색
            while True:
                value = input("검색어>")
                if value =="":
                    input("메뉴로 돌아가려면 아무 키나 누르세요.")
                    break
                sales = sale_list(value)
                for sale in sales:
                    sale.print()
            pass
        elif menu =="3":#매출목록
            sales = sale_list("")
            for sale in sales:
                sale.print()
            input("메뉴로 돌아가려면 아무 키나 누르세요.")
            pass
        elif menu =="4":#매출수정
            input("메뉴로 돌아가려면 아무 키나 누르세요.")
            pass
        elif menu =="5":#매출삭제
            input("메뉴로 돌아가려면 아무 키나 누르세요.")
            pass
        else:
            print("[0]~[5]의 메뉴를 선택하세요!")
            input("메뉴로 돌아가려면 아무 키나 누르세요.")
            continue



if __name__=="__main__":
    saleMenu()
