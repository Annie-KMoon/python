import os, pandas as pd

#전역변수:
file_pro = '교수.csv'
file_stu = '학생.csv'

#숫자입력
def inputNum(title):
    while True:
        num = input(title)
        if num =='':
            return ''
        
        elif num.isnumeric():
            return int(num)
        
        else:
            print("숫자로 입력하세요!")

#교수목록
def pro_list():
    pro = pd. read_csv(file_pro, index_col='교수번호')
    for idx,row in pro.iterrows():
        print(f"이름:{row['교수이름']}({idx}) 학과:{row['교수학과']} 임용일:{row['임용일']} 교수직급:{row['교수직급']} 급여:{row['급여']:,}원")

#교수검색
def pro_search(code):
    pro = pd.read_csv('교수.csv', index_col='교수번호')
    stu = pd.read_csv('학생.csv', index_col='학생번호')
    cou = pd.read_csv('강좌.csv', index_col='강좌번호')
    if code in pro.index:
        pro_row=pro.loc[code]
        print(code, pro_row['교수이름'], pro_row['교수학과'])
        
        print('[담당강좌]--------------------------------------')
        filt = cou['담당교수']==code
        cou_rows = cou[filt]
        for idx, row in cou_rows.iterrows():
            print(idx, row['강좌이름'], row['강의시수'])
            
        print('[담당학생]--------------------------------------')
        filt = stu['지도교수'] == code
        stu_rows = stu[filt]
        for idx, row in stu_rows.iterrows():
            print(idx, row['학생이름'], row['학생학과'], row['학년'])
    else:
        print("해당 교수 정보가 없습니다.")

#학생목록
def stu_list():
    stu = pd.read_csv('학생.csv')
    pro = pd.read_csv('교수.csv')
    merge = stu.merge(pro, left_on='지도교수', right_on='교수번호')
    merge = merge.sort_values('학생이름') #이름순출력
    for idx, row in merge.iterrows():
        print(f"{idx}){row['학생이름']}({row['학생번호']}) 학과:{row['학생학과']}  학년:{row['학년']} 생년월일:{row['생년월일']} 담당교수:{row['교수이름']}")

def stu_search(code):
    stu = pd.read_csv('학생.csv', index_col='학생번호')
    pro = pd.read_csv('교수.csv', index_col='교수번호')
    cou = pd.read_csv('강좌.csv', index_col='강좌번호')
    enroll = pd.read_csv('수강.csv', index_col=['학생번호','강좌번호'])
    enroll.fillna(0, inplace=True)
  
    if code in stu.index:
        stu_row=stu.loc[code]
        advisor=stu_row['지도교수']
        pro_row=pro.loc[advisor]
        # enroll_rows=enroll.loc[code]
        print(stu_row['학생이름'], stu_row['학생학과'], pro_row['교수이름'])
        print('\n수강 과목')
        print('-'*50)
        enroll_rows=enroll.loc[code]

        sum = 0
        for idx, row in enroll_rows.iterrows():
            cou_row=cou.loc[idx]
            print(idx,cou_row['강좌이름'],row["신청일"], row["점수"])
            sum+=row['점수']
        avg=sum/len(enroll_rows)
        print(f'평균:{avg:.2f}\n')
        
    
    else:
        print("해당 학생정보가 없습니다.")

def cou_list():
    cou = pd.read_csv('강좌.csv')
    pro = pd.read_csv('교수.csv')
    merge =cou.merge(pro, left_on='담당교수', right_on='교수번호')
    # merge = merge.sort_values('강좌이름') #이름순출력
    merge = merge.sort_index()
    for idx, row in merge.iterrows():
        print(f"{idx+1}){row['강좌이름']}({row['강좌번호']}) 담당교수:{row['교수이름']} 강의실:{row['강의실']}  강의시수:{row['강의시수']} ")

def cou_search(code):
    stu = pd.read_csv('학생.csv', index_col='학생번호')
    pro = pd.read_csv('교수.csv', index_col='교수번호')
    enroll = pd.read_csv('수강.csv', index_col=['강좌번호', '학생번호'])
    enroll.fillna(0, inplace=True)
    cou = pd.read_csv('강좌.csv', index_col='강좌번호')
    
    if not code in cou.index:
        print('해당 학번이 존재하지 않습니다.')
        return
    
    cou_row = cou.loc[code]
    advisor = cou_row['담당교수']
    pro_row = pro.loc[advisor]
    print(cou_row['강좌이름'],cou_row['강의실'], pro_row['교수이름'])
    
    print('\n수강학생')
    print('-' * 50)
    enroll_rows = enroll.loc[code]

    sum = 0
    for idx, row in enroll_rows.iterrows():
        stu_row = stu.loc[idx]
        print(idx, stu_row['학생이름'], row['신청일'], row['점수'])
        sum += row['점수']
    avg = sum/len(enroll_rows)
    print(f'평균:{avg:.2f}\n')

# def cou_search(code):
#     stu = pd.read_csv('학생.csv', index_col='학생번호')
#     pro = pd.read_csv('교수.csv', index_col='교수번호')
#     cou = pd.read_csv('강좌.csv', index_col='강좌번호')
#     enroll = pd.read_csv('수강.csv', index_col=['강좌번호','학생번호'])
#     enroll.fillna(0, inplace=True)
  
#     if code in cou.index:
#         cou_row=cou.loc[code]
#         advisor=cou_row['담당교수']
#         pro_row=pro.loc[advisor]
#         enroll_rows=enroll.loc[code]
#         print (cou_row['강좌이름'],cou_row['강의실'], pro_row['교수이름'])
#         print('\n수강학생')
#         print('-'*50)
#         enroll_rows=enroll.loc[code]

#         sum = 0
#         for idx, row in enroll_rows.iterrows():
#             stu_row=stu.loc[idx]
#             print(idx,stu_row['학생이름'],row["신청일"], row["점수"])
#             sum+=row['점수']
#         avg=sum/len(enroll_rows)
#         print(f'평균:{avg:.2f}')

#     else:
#         print("해당 강좌정보가 없습니다.")
#         return
    
    

while True:
    os.system('cls')
    print('='*50)
    print('학사관리')
    print('='*50)
    print('[1]교수목록')
    print('[2]교수검색')
    print('[3]학생목록')
    print('[4]학생검색')
    print('[5]강좌목록')
    print('[6]강좌검색')
    print('[0]종료')
    print('-'*50)


    menu = input("메뉴선택>")
    if menu =="0":
        input("프로그램을 종료합니다. 아무키나 누르세요.")
        break
    elif menu =='1':#교수목록
        pro_list()
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu =='2':#교수검색-교수 담당 과목/학생 출력
        while True:
            code = inputNum("교수번호>")
            if code =="": 
                input("검색을 종료합니다.")
                break
            pro_search(code)

    elif menu =='3': #학생목록
        stu_list()
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu =='4':
        while True:
            code = inputNum("학생번호>")
            if code =="": 
                input("검색을 종료합니다.")
                break
            stu_search(code)

    elif menu =='5':
        cou_list()
        input("메뉴로 돌아가려면 아무키나 누르세요.")

    elif menu =='6':
        while True:
            code = input("강좌번호>")
            if code =="": 
                input("검색을 종료합니다.")
                break
        cou_search(code.upper())

    else:
        input("0~6번 메뉴를 선택하세요!")



