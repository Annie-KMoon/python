from function import *
from jusofile import *

def newSeq(): #새로운 번호 리턴 함수
    list = fileRead() #파일 리스트 데이터 리드
    if len(list) ==0: return 1 #번호 없는 경우 1부터
    seqs = [person.seq for person in list] #여러개 [], 숫자만, seq들 입력
    # max_seq = max(seqs)+1
    return max(seqs)+1

def searchSeq(seq): #삭제/수정 번호 찾기 함수
    list = fileRead()
    result = [p for p in list if p.seq ==seq]
    if len(list) > 0: return result[0] #result=0값X seq는 고유값 0

while True:
    menuPrint("주소관리")
    menu =input("메뉴선택>")
    if menu == "0":
        print("프로그램을 종료합니다.")
        break

    elif menu=="1": #입력
        person = Person()
        person.seq = newSeq()
        print(f"번호>{person.seq}")
        if person.seq == "" : 
            print("메뉴로 돌아갑니다.")
            continue
        person.name = input("이름>")
        if person.name == "":
            print("메뉴로 돌아갑니다.")
            continue
        person.address = input("주소>") #추후 수정되도록 빈칸 가능하게
        fileAppend(person)
        person.print()
        print("입력성공!") #입력정보 확인 출력

    elif menu=="2": #검색(이름, 주소 사용)
        while True:
            value = input("검색어>")
            if value == "": 
                print("검색 종료 후 메뉴로 돌아갑니다.")
                break
            list = fileRead() #데이터 읽기 위한 ()
            result = [person for person in list if person.name.find(value)!=-1 or person.address.find(value)!=-1]
            if len(result) == 0:
                print(f"검색결과가 없습니다.")
                continue
            for person in result:
                person.print()

    elif menu=="3": #목록
        list = fileRead()
        for person in list:
            person.print()
    
    elif menu=="4": #삭제
        list = fileRead()
        seq = inputNum("삭제번호>")
        # person = search(seq)
        # if person == None:
        #     print("삭제할 번호가 없습니다.")
        result = [p for p in list if p.seq ==seq] #삭제번호/ 한줄 if문,list*
        if len (result)==0:
            print("삭제할 번호가 없습니다.")
            continue
        person = result[0] #찾은 정보
        person.print() #정보출력
        sel = input("삭제하시겠습니까?(Y/N)>")
        if sel == 'Y' or sel == 'y': #삭제 외 데이터만 rewrite
            result = [p for p in list if p.seq !=seq]
            fileWrite(result)
            print("삭제 성공!")
        else:
            print("삭제가 취소되었습니다. 메뉴로 돌아갑니다.")
            continue

    elif menu=="5": #수정 OK
        list = fileRead()
        # seq = int(input("수정번호>"))
        # update(seq)

        seq = inputNum("수정번호>")
        result = [p for p in list if p.seq == seq] #seq동일시 리스트에서p값 가져와서 리스트
        if len(result)==0:
            print("수정할 번호가 없습니다.")
            continue
        person = result[0] #검색된 하나의 값
        person.print()
        sel = input("수정하시겠습니까?(Y/N)>")
        if sel == "y" or sel == "y":
            name = input(f"이름:{person.name}>")
            if name!="": person.name = name
            address = input(f"주소:{person.address}>")
            if address!="": person.address = address
            person.print()
            fileWrite(list)
            print("정보수정완료!")
        else:
            print("수정이 취소되었습니다. 메뉴로 돌아갑니다.")
            continue

    else:
        print("0~5의 메뉴를 선택하세요.")
        continue
    