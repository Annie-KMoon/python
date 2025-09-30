#성적관리
import pandas as pd
import numpy as np
import os

score_name = 'data/학생성적.csv'
score = pd.read_csv(score_name)

info_name = 'data/학생정보.csv'
info = pd.read_csv(info_name)

def inputNum(title):
    while True:
        num = input(title)
        if num =='':
            return 0
        
        elif not num.isnumeric():
            print("숫자로 입력하세요!")
            continue
        
        else:
            return int(num)

while True:
    os.system('cls')
    print('-'*48)
    print('*******************성적관리*******************')
    print('-'*48)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
    print('-'*48)
    menu = input("메뉴선택>")
    if menu == "0":
        input("프로그램을 종료합니다. 아무키나 누르세요.")
        break

    elif menu == "1": #등록
        idx = len(score)
        no = f'{idx+1}번'
        print(f'지원번호>{no}')
        num1 = inputNum("국어>")
        num2 = inputNum("영어>")
        num3 = inputNum("수학>")
        num4 = inputNum("과학>")
        num5 = inputNum("사회>")
        score.loc[idx]=[no,num1,num2,num3,num4,num5]
        sel = input("등록하시겠습니까?(N/Y)>")
        if sel =="Y" or sel =="y":
            score.to_csv(score_name, index=False) #인덱스 중복저장 안되도록
            input("성적 등록 성공!")
        else:
            input("등록을 종료하고 메뉴로 돌아갑니다.")
            break

    elif menu == "2": #목록
        print(score)
        # for i in range(0, len(score)):
        #     row = score.loc(i)
        #     print(f"{row['지원번호']},{row['국어']}")
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu == "3": #검색
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu == "4": #삭제
        idx = input('삭제지원번호>')
        idx = idx+ '번'
        filt = score['지원번호']==idx
        search = score[filt].index
        if len(search) == 0:
            print("해당 번호가 없습니다.")
        else:
            print(score[filt])
            sel = input("삭제하시겠습니까?(N/Y)>")
            if sel == "Y" or sel =="y":
                score.drop(index=search, inplace=True)
                score.to_csv(score_name, index=False) #인덱스 중복저장 안되도록
                print("삭제완료!")
            else:
                input("삭제를 종료하고 메뉴로 돌아갑니다.")
                continue
        
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu == "5": #수정
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    else:
        input("0~5번 메뉴를 선택하세요.")


