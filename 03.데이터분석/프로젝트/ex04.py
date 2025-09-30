#학생정보관리

import os
import pandas as pd
from ex05 import *

#전역변수
file_name = 'data/학생정보.csv'

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
        

while True:
    #전역변수
    info = pd.read_csv(file_name, index_col='지원번호')
    info.fillna('', inplace=True)
    cols = info.columns
    os.system('cls')

    print('-'*48)
    print('*******************학생정보*******************')
    print('-'*48)
    print('1.등록|2.목록|3.검색|4.삭제|5.수정|6.성적관리|0.종료')
    print('='*48)

    menu = input("메뉴선택>")
    if menu == "0": #종료
        input("프로그램을 종료합니다. 아무키나 누르세요.")
        break

    elif menu == "1": #등록
        new_no = info.index.max()+1
        print(f'신규지원번호>{new_no}')
        name = input("이름>")
        if name == "": 
            input("저장되지 않고 메뉴로 돌아갑니다.")
            continue
        school = input("학교>")
        height = inputNum("키>")
        if height =="": height = 0
        sw = input("SW특기>")
        info.loc[new_no]=[name, school, height, sw]

        sel = input("등록하시겠습니까?(N/Y)>")
        if sel =="Y" or sel =="y":
            info.to_csv(file_name) 
            print("등록 성공!")
            input("종료하고 메뉴로 돌아갑니다.")
        else:
            input("등록을 취소하고 메뉴로 돌아갑니다.")

    elif menu == "2": #목록
        for idx in info.index:
            row = info.loc[idx]
            print(f'지원번호:{idx}', end=" ")
            for col in cols:
                print(f'{col}:{row[col]}', end=' ')
            print()
            print('-'*50)
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu == "3": #검색
        while True:
            sel = input("1:이름|2:학교|3:SW특기>")
            if sel == "": 
                input("검색을 종료하고 메뉴로 돌아갑니다..")
                break
            word = input("검색어>")
            if word == "": 
                input("검색을 종료하고 메뉴로 돌아갑니다..")
                break            
            elif sel =='1': #이름 검색
                filt = info['이름'].str.contains(word)
            elif sel == '2':
                filt = info['학교'].str.contains(word)
            elif sel == '3':
                word=word.upper()
                filt = info['SW특기'].str.upper().str.contains(word)
            idxs = info[filt].index
            if len(idxs)==0:
                print("검색하신 정보가 없습니다.")
            else: 
                for idx in idxs:
                    row = info.loc[idx]
                    print(f'지원번호:{idx}', end=" ")
                    for col in cols:
                        print(f'{col}:{row[col]}', end=' ')
                    print()
                    print('-'*50)
            # else:
            #     print("1~3을 선택하세요!")


    elif menu == "4": #삭제
        no = inputNum("삭제할 지원번호>")
        if no in info.index:
            row = info.loc[no]
            for col in cols:
                print(f'{col}:{row[col]}', end=' ')
            print()
            sel = input("삭제하시겠습니까?(N/Y)>")
            if sel =="Y" or sel =="y":
                info.drop(index=no, inplace=True)
                info.to_csv(file_name)
                print("삭제완료!")
                input("종료하고 메뉴로 돌아갑니다.")
            else:
                input("삭제를 취소하고 메뉴로 돌아갑니다.")
        else:
            input("삭제할 데이터가 없습니다. 삭제를 취소하고 메뉴로 돌아갑니다.")
        # if no == "":
        #     input("삭제를 종료하고 메뉴로 돌아갑니다.")


    elif menu == "5": #수정
       no = inputNum("수정할 지원번호>")
       if no in info.index:
            row = info.loc[no]
            name = input(f"이름:{row['이름']}>")
            if name =="":
                name =row['이름']
            school = input(f"학교:{row['학교']}>")
            if school =="":
                school =row['학교']
            height = inputNum(f"키:{row['키']}>")
            if height =="":
                height =row['키']  
            sw = input(f"SW특기:{row['SW특기']}>")
            if sw =="":
                sw =row['SW특기']
            sel = input("수정하시겠습니까?(N/Y)>")
            if sel =="Y" or sel =="y":
                info.loc[no]=[name, school, height, sw]
                info.to_csv(file_name)
                print("수정완료!")
                input("종료하고 메뉴로 돌아갑니다.")
            else:
                input("수정을 취소하고 메뉴로 돌아갑니다.")                                                          
       else:
           input("수정할 데이터가 없습니다. 삭제를 취소하고 메뉴로 돌아갑니다.")          

    elif menu =="6": #성적관리
        submenu()

    else:
        input("0~6번 메뉴를 선택하세요!")




