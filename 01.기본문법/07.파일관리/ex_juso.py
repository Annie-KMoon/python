import os
path =os.path.dirname(os.path.realpath(__file__)) #파일 위치 구하기

# print('현재패스:'+path)

#주소 관리를 위한 클래스(변수 여러개, 객체간 데이터) -객체지향어(OOT)
class Person:
    def __init__(self): #객체생성자
        self.seq = 0 #속성(seq,name,address)
        self.name =""
        self.address="경기도 광명시"

    def print(self): #메서드(함수)
        print(f"번호:{self.seq}, 이름:{self.name}, 주소:{self.address}")

file_name = path+"/ex_juso0825.txt"

#파일 데이터(객체) 추가 함수
def fileAppend(person): #1명외 수정시
    with open(file_name, 'a',encoding='utf-8') as file: #as 파일별명
        # for person in list: #필요없는 라인?
        file.write(f"{person.seq},{person.name},{person.address}\n")

#파일 데이터(객체) 다시쓰기(수정) 함수
def fileWrite(list): #person>list?
    with open(file_name, 'w',encoding='utf-8') as file: #as 파일별명
        for person in list: #이 라인 추가
            file.write(f"{person.seq},{person.name},{person.address}\n")

#파일에서 데이터 읽기 함수
def fileRead(): #전체 읽기:매개변수X, ()
    list = []
    with open(file_name,'r',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            items = line.split(",")
            person =Person()
            person.seq = int(items[0]) #비교시 숫자로 전환
            person.name = items[1]
            person.address = items[2].replace("\n","") #\n을 공백으로 교체하여 read시 줄바꿈 정리
            list.append(person) #리스트로 append
        return list
        # print(f"번호:{items[0]}, 이름:{items[1]}, 주소:{items[2]}")

#데이터 추가 테스트-데이터추가함수 
def append():
    person = Person() #person 객체생성
    person.seq = 5
    person.name='이순신'
    person.address = '인천 서구 경서동'
    person.print() #프린트 메서드 출력
    fileAppend(person) #실행시 append()


#fileRead()함수테스트-목록출력함수
def list():
    list = fileRead()
    for person in list:
        person.print()

#검색함수(seq/이름)
def search(type, value): #1-번호, 2-이름, 3-주소로 설정
    list = fileRead() #전체 파일 로드
    result = []
    if type == 1: #seq로 검색
        result = [person for person in list if person.seq==value]
    elif type == 2: #name으로 검색
        result = [person for person in list if person.name.find(value)!=-1] #부분일치 find
    elif type == 3: #address으로 검색
        result = [person for person in list if person.address.find(value)!=-1]  
    return result

#검색함수 테스트- 검색 출력함수
#     result = search(3,"부산")
#     if len(result)==0:
#         print("검색결과가 없습니다.")
#     else:
#         for person in result:
#             person.print()

#삭제함수 
def delete(seq):
    list = fileRead()
    result = [person for person in list if person.seq != seq]
    # if len(result)==0: print("검색결과가 없습니다.")
    # else:
    fileWrite(result)
# delete(5)

#수정함수
def update(seq):
    list = fileRead()
    result = [person for person in list if person.seq == seq]
    # result = search(1,seq)
    if len(result)==0: print("검색결과가 없습니다.")
    else:
        person = result[0]
        # person.print()
        name = input(f"이름:{person.name}>")
        if name !="": person.name = name
        address = input(f"주소:{person.address}>")
        if address !="": person.address = address
        fileWrite(list)
        person.print() #구조 주의
        

seq = int(input("수정번호>"))
update(seq)
