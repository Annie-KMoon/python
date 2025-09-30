from function import *
from jusoDB import *

while True:
    menuPrint("주소관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print("프로그램을 종료합니다.")
        break

    elif menu == "1":#입력 (#번호 자동생성) OK
        rows = list()
        print(f"현재 {len(rows)}개의 데이터가 있습니다.")
        p = Person()
        p.name = input("이름>")
        p.address = input("주소>")
        insert(p)
        print("입력 성공!")
        rows=list()
        print(f"입력 후 현재 {len(rows)}개의 데이터가 있습니다.")

    elif menu == "2": #검색
       while True:
           value = input("검색어>")
           rows = search(value)
           if value == "": 
               print("검색을 종료하고 메뉴로 돌아갑니다.")
               break
           elif len(rows)==0:
                print("검색 내용이 없습니다.")
                continue           
           else:
               for row in rows:
                   person = Person()
                   person.seq = row[0]
                   person.name = row[1]
                   person.address = row[2]
                   person.print()
            

    elif menu == "3":#목록 OK
       rows = list()
       for row in rows:
           person = Person()
           person.seq = row[0]
           person.name = row[1]
           person.address = row[2]  
           person.print()  

    elif menu == "4":#삭제 OK
        seq = input("삭제번호>")
        row = read(int(seq))
        if row == None:
            print("삭제번호가 없습니다.")
        else:
            p = Person()
            p.seq=row[0]
            p.name=row[1]
            p.address=row[2]
            p.print()
            sel = input("삭제하시겠습니까?(Y/N)>")
            if sel =="y" or sel =="Y":
                delete(seq)
                p.print()
                print("삭제완료!")
            else:
                print("삭제가 취소되어 메뉴로 돌아갑니다.")
                continue

    elif menu == "5":#수정
        p = Person()
        p.seq = inputNum("수정번호>")
        row = read(p.seq)
        if row == None:
            print("수정 번호가 없습니다.")
        else:
            p.name = row[1]
            p.address = row[2]
            name = input(f"이름 수정:{p.name}>")
            if name!="": p.name = name
            address = input(f"이름 수정:{p.address}>")
            if address!="": p.address = address
            
            sel = input("수정하시겠습니까?(Y/N)>")
            if sel =="y" or sel =="Y":
                update(p)
                p.print()
                print("수정완료!")
            else:
                print("수정이 취소되어 메뉴로 돌아갑니다.")
                continue          

    else:
        print("0~5의 메뉴를 골라주세요!")