from score import Score
from function import *


def insert(list):
    score = Score()
    score.no = input("학번>")
    score.name = input("이름>")
    score.kor = int(input("국어>"))
    score.eng = int(input("영어>"))
    score.mat = int(input("수학>"))
    print(score.dict())
    list.append(score.dict()) #입력받은 데이터 dict로저장


def search(name):
    for s in scores:
        if name == s['name']:
            return s

scores = [
    {'no':'01','name':'김일영','kor':100,'eng':100,'mat':100,'avg':100,'result':'PASS'}
] 

while True:
    menuPrint("성적관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print("프로그램을 종료하겠습니다.")
        break

    if menu =="1": #입력
        insert(scores)
        print("성적 입력이 완료되었습니다.")
#성적 ""기재시?

    elif menu =="2": #검색
        no = input("검색학번>")
        isFind = False
        for s in scores:
            if no==s['no']:
                print(f"no:{s['no']},이름:{s['name']},국어:{s['kor']},영어:{s['eng']},수학:{s['mat']},평균:{s['avg']:.2f},이수:{s['result']}")
                isFind = True
        if isFind ==False:
            print(f"no:{s['no']},이름:{s['name']},국어:{s['kor']},영어:{s['eng']},수학:{s['mat']},평균:{s['avg']:.2f},이수:{s['result']}")

    elif menu =="3": #목록
        for s in scores:
            print(f"no:{s['no']},이름:{s['name']},국어:{s['kor']},영어:{s['eng']},수학:{s['mat']},평균:{s['avg']:.2f},이수:{s['result']}")

    elif menu =="4":#삭제
        no = input("삭제번호")
        for idx, s in enumerate(scores):
            if no == s['no']:
                scores.pop(idx)

    elif menu =="5":#수정
        name = input("수정이름")
        if name == "":
            print("메뉴로 돌아갑니다.")
            continue
        idx = search(name)
        if idx == s['name']:
            print(f"no:{s['no']}")
            print(f"이름:{s['name']}")   
            kor = inputNum(f"국어:{s['kor']}")         
            if kor !="": s['kor']=kor
            print("성정수정완료!")    
            eng = inputNum(f"영어:{s['eng']}")         
            if eng !="": s['eng']=eng
            print("성정수정완료!")    
            mat = inputNum(f"수학:{s['mat']}")   
            if mat !="": s['mat']=mat
            print("성정수정완료!")                  
        elif idx == None:
            print(f'{name}의 정보가 없습니다.')
            continue
    
    else:
        print("0~5번의 메뉴를 선택하세요.")
        continue