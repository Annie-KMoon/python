from function import *

file_name = 'C:/python/01.기본문법/data/juso.txt'

#함수
def insert(no,name, phone, address):  #외부파일로 작성해도 되는 함수/ 입력함수, 파일에 데이터저장
    with open(file_name, 'a', encoding='utf-8') as file:
        no= int(maxNo())+1 #int로 전환
        file.write(f"{no},{name},{phone},{address}\n") #기존 txt 파일과 포맷유지
        print("등록완료!")

def read(): #파일에 데이터를 읽어서 list 리턴 읽기함수/ 목록출력
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        list = [] #데이터 저장
        for line in lines:
            items = line.split(",") # csv 구분된 표시로 체크
            no = items[0]
            name = items[1]
            phone= items[2]
            address=items[3]
            item = {'no':no, 'name':name, 'phone':phone, 'address':address}
            list.append(item) #item을 list에 추가
        return list
        # return list #종료 후 리스트로 return   

def search(name): #이름을 받아서 검색결과를 dict로 리턴
    items = read()
    list =[]
    for item in items:
        if item['name'].find(name) !=-1:
            list.append(item) #item dict-list로 append
    return list #찾은 결과가 있는 list로 리턴

#가장 큰 번호를 찾아서 리턴하는 함수
def maxNo():
    items = read()
    nos =[]
    for item in items:
        nos.append(int(item['no'])) #no가 str이라 int로 처리
    if len(nos)==0:
        return 0
    else:
        return max(nos)

while True:
    menuPrint("주소관리")
    menu = input("메뉴선택>")
    if menu =="0": #종료
        print("프로그램을 종료합니다.")
        break

    elif menu =="1": #입력
        no = maxNo()+1
        print(f"신규번호:{no}")
        name = input("이름>")
        if name =="": continue
        phone = input("전화>")
        address = input("주소>")
        insert(no,name,phone,address)
        
    elif menu =="2": #검색
        name = input("검색이름>")
        list = search(name)
        if len(list)==0:
            print(f"'{name}'데이터가 없습니다.")
            continue
        for item in list: #검색리스트안 체크
            if item['name'].find(name) !=-1: #찾는것.찾아지는곳주의
                print(f"no:{item['no']},이름:{item['name']},전화번호:{item['phone']},주소:{item['address']}",end="")

    elif menu =="3": #목록
        items = read()
        for item in items:
            print(f"no:{item['no']},이름:{item['name']},전화번호:{item['phone']},주소:{item['address']}",end="")


    elif menu =="4": #삭제
        pass

    elif menu =="5": #수정
        pass

    else:
        print("0~5의 메뉴를 고르세요!")            