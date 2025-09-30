#성적관리
import os
import pandas as pd
# import numpy as np

#전역변수
file_name = 'data/학생성적.csv'
score = pd.read_csv(file_name)
cols = score.columns

# info_name = 'data/학생정보.csv'
# info = pd.read_csv(info_name)

def inputNum(title):
    while True:
        num = input(title)
        if num =='':
            return ''
        
        elif not num.isnumeric():
            print("숫자로 입력하세요!")
            continue
        
        else:
            return int(num)

def sort_List():
    while True:
        score = pd.read_csv(file_name)
        for idx, col in enumerate(cols):
            print(f'{idx}:{col}', end='|')
        print()
        sel = inputNum('선택>')
        if sel=="": break
        score = score.sort_values(cols[sel], ascending=False)
        for idx in score.index: #인덱스 반복#주의
            row = score.loc[idx]
            for col in cols:
                print(f'{col}:{row[col]}', end="  ")
            print()
        # if sel==0:
        #     score = score.sort_values('지원번호')
        # elif sel==1:
        #     score = score.sort_values('국어')            
        # elif sel==1:
        #     score = score.sort_values('영어')   
        # elif sel==1:
        #     score = score.sort_values('수학')   
        # elif sel==1:
        #     score = score.sort_values('과학')   
        # elif sel==1:
        #     score = score.sort_values('사회')                                       


while True:
    score = pd.read_csv(file_name)
    os.system('cls')
    print('-'*48)
    print('*******************성적관리*******************')
    print('-'*48)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
    print('='*48)
    menu = input("메뉴선택>")
    if menu == "0":
        input("프로그램을 종료합니다. 아무키나 누르세요.")
        break

    elif menu == "1": #등록
        index = max(score.index)+1
        no = score['지원번호'].max()+1
        grade = []
        for idx, col in enumerate(cols):
            if idx==0:
                print(f'지원번호>{no}')
            else:
                num = inputNum(f'{col}>')
                if num =="": num=0
                grade.append(num)
        score.loc[index]=[no, grade[0],grade[1],grade[2],grade[3],grade[4]]
        sel = input("등록하시겠습니까?(N/Y)>")
        if sel =="Y" or sel =="y":
            score.to_csv(file_name, index=False) 
            print("등록 성공!")
            input("종료하고 메뉴로 돌아갑니다.")
        else:
            input("등록을 취소하고 메뉴로 돌아갑니다.")

    elif menu == "2": #목록
        sort_List()
        # for idx in range(len(score)):
        #     row = score.loc[idx]
        #     for col in cols:
        #         print(f'{col}:{row[col]}', end="  ")
        #     print()
        # input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu == "3": #검색
        while True:
            no = inputNum('검색할 지원번호>')
            if no == "":
                input("검색을 종료하고 메뉴로 돌아갑니다.")
                break
            filt = score['지원번호']==no
            idxs = score[filt].index
            if len(idxs)==0:
                print("검색하신 지원번호가 없습니다.")
            else:
                row = score.loc[idxs[0]]
                for col in cols:
                    print(f'{col}:{row[col]}', end="  ")
                print()

    elif menu == "4": #삭제
        no=inputNum('삭제할 지원번호>')
        if no == "":
            input("삭제를 종료하고 메뉴로 돌아갑니다.")
        filt = score['지원번호']==no
        idx = score[filt].index
        if len(idx)==0:
            input("삭제할 데이터가 없습니다.")
        else:
            row = score.loc[idx[0]] #idx값1
            for col in cols:
                print(f'{col}:{row[col]}', end="  ")
            print()
            sel = input("삭제하시겠습니까?(N/Y)>")
            if sel =="Y" or sel =="y":
                score.drop(index=idx[0], inplace=True)
                score.to_csv(file_name, index=False)
                print("삭제완료!")
                input("종료하고 메뉴로 돌아갑니다.")
            else:
                input("삭제를 취소하고 메뉴로 돌아갑니다.")

    elif menu == "5": #수정
        no=inputNum('수정할 지원번호>')
        if no == "":
            input("수정을 종료하고 메뉴로 돌아갑니다.")
        idx = score[score['지원번호']==no].index
        if len(idx)==0:
            input("수정할 데이터가 없습니다.")
        else:
            row = score.loc[idx[0]] #idx값1
            grade = [] #수정값넣을리스트
            for index, col in enumerate(cols): #지원번호 입력 안되도록
                if index ==0: continue
                num = inputNum(f'{col}:{row[col]}>')
                if num =="":
                    num=row[col]
                grade.append(num)
            
            sel = input("수정하시겠습니까?(N/Y)>")
            if sel =="Y" or sel =="y":
                score.loc[idx[0]]=[no, grade[0],grade[1],grade[2],grade[3],grade[4]]
                score.to_csv(file_name, index=False)
                print("수정완료!")
                input("종료하고 메뉴로 돌아갑니다.")
            else:
                input("수정을 취소하고 메뉴로 돌아갑니다.")

    else:
        input("0~5번 메뉴를 선택하세요!")


