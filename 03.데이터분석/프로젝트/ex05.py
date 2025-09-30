#학생성적관리
import os
import pandas as pd

file_info='data/학생정보.csv'
file_score='data/학생성적.csv'

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

def submenu():
    while True:
        info= pd.read_csv('data/학생정보.csv', index_col='지원번호')
        score=pd.read_csv('data/학생성적.csv', index_col='지원번호')
        #두 파일 조인
        df = info.join(score)
        #총점/평균
        df['총점']= df.apply(lambda x:sum(x['국어':'사회']), axis=1)
        df['평균'] = df['총점']/5
        #Null값 채우기
        df.fillna(0, inplace=True)

        cols = ['국어','영어','수학','사회','과학']
        
        os.system('cls')
        print('-'*48)
        print('*******************성적관리*******************')
        print('-'*48)
        print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
        print('='*48)
        menu = input("메뉴선택>")
        if menu == "0": #종료
            input("프로그램을 종료합니다. 아무키나 누르세요.")
            break

        elif menu == "1": #등록
            no = inputNum("지원번호>")
            if not no in info.index:
                input("등록되지 않은 지원번호 입니다.")
            elif no in score.index:
                input("이미 등록된 성적 데이터입니다.")
            else:
                row = info.loc[no]
                print(f'이름:{row["이름"]}')
                grade =[]
                for col in cols:
                    num = inputNum(f'{col}>')
                    if num == "": num = 0
                    grade.append(num)
                score.loc[no] = grade
                sel = input("등록하시겠습니까?(N/Y)>")
                if sel =="Y" or sel =="y":
                    score.to_csv(file_score)
                    input("성적등록완료!")
                    print("종료하고 메뉴로 돌아갑니다.")
                else:
                    input("등록을 취소하고 메뉴로 돌아갑니다.")

        elif menu == "2": #목록
            while True:
                sel = inputNum("0.입력순|1.최신입력순|2.이름순|3.성적순>")
                if sel =="":
                    input("목록을 종료하고 메뉴로 돌아갑니다.")
                    break
                elif sel ==0: df=df.sort_index(ascending=True)
                elif sel ==1: df=df.sort_index(ascending=False)
                elif sel ==2: df=df.sort_values("이름",ascending=True)
                elif sel ==3: df=df.sort_values("평균", ascending=False)
                for idx in df.head().index: #head()추가시 ()개에 대한 인덱스값만 반복
                    row = df.loc[idx]
                    print(f"지원번호:{idx:02d}", end=" ")
                    print(f"이름:{row['이름']}", end=" ")
                    print(f"학교:{row['학교']}", end=" ")                    
                    for col in cols:
                        print(f'{col}:{row[col]:.0f}', end =" ")
                    print(f'평균:{row["평균"]:.2f}')
                    print('-'*50)

        elif menu == "3": #검색
            while True:
                sel = inputNum("1:지원번호|2:학교|3:이름>")
                if sel == "": 
                    input("검색을 종료하고 메뉴로 돌아갑니다..")
                    break
                # word = input("검색어>")
                # if word == "": 
                #     input("검색을 종료하고 메뉴로 돌아갑니다..")
                #     break
                elif sel ==1: #지원번호 검색
                    no = inputNum("검색할 지원번호>")
                    if not no in df.index:
                        input("검색하신 지원번호가 없습니다.")
                    else:
                        row = df.loc[no]
                        print(f'지원번호:{no} 이름:{row["이름"]} 학교:{row["학교"]} 평균:{row["평균"]:.2f}')

                elif sel ==2: #학교
                    word = input("검색어>")
                    if word=="": 
                        input("검색을 종료하고 메뉴로 돌아갑니다.") 
                        continue
                    filt = df['학교'].str.contains(word)
                    if len(df[filt].index)==0:
                        print("검색하신 결과가 없습니다.")
                        continue #생략가능
                    for idx in df[filt].index:
                        row = df.loc[idx]
                        print(f'지원번호:{idx} 이름:{row["이름"]} 학교:{row["학교"]} 평균:{row["평균"]:.2f}')

                elif sel ==3: #이름
                    word = input("검색어>")
                    if word=="": 
                        input("검색을 종료하고 메뉴로 돌아갑니다.") 
                        continue
                    filt = df['이름'].str.contains(word)
                    if len(df[filt].index)==0:
                        print("검색하신 결과가 없습니다.")                  
                    for idx in df[filt].index:
                        row = df.loc[idx]
                        print(f'지원번호:{idx} 이름:{row["이름"]} 학교:{row["학교"]} 평균:{row["평균"]:.2f}')


        elif menu == "4": #삭제
            no = inputNum("삭제할 지원번호>")
            if no =="":
                input("삭제를 종료하고 메뉴로 돌아갑니다.")
            elif not no in info.index:
               input("등록되지 않은 지원번호 입니다.")
            elif not no in score.index:
                input("등록된 성적이 없습니다.")
            else:
                row = df.loc[no]
                print(f"이름:{row['이름']}")
                for col in cols:
                    print(f"{col}:{row[col]}", end=" ")
                sel = input("삭제하시겠습니까?(N/Y)>")
                if sel =="Y" or sel =="y":
                    score.drop(index=no, inplace=True)
                    score.to_csv(file_score)
                    print("삭제완료!")
                    input("종료하고 메뉴로 돌아갑니다.")
                else:
                    input("삭제를 취소하고 메뉴로 돌아갑니다.")                    

        elif menu == "5": #수정
            no = inputNum("수정할 지원번호>")
            if no =="":
                input("수정을 종료하고 메뉴로 돌아갑니다.")
            elif not no in info.index:
               input("등록되지 않은 지원번호 입니다.")
            elif not no in score.index:
                input("등록된 성적이 없습니다.")
            else:
                row = score.loc[no]
                print(f"이름>{info.loc[no,'이름']}")
                grade=[]
                for col in cols:
                    num = inputNum(f'{col}:{row[col]}>')
                    if num=="": num=row[col]
                    grade.append(num)
                sel = input("수정하시겠습니까?(N/Y)>")
                if sel =="Y" or sel =="y":
                    score.loc[no] = grade
                    score.to_csv(file_score)
                    print("수정완료!")
                    input("종료하고 메뉴로 돌아갑니다.")
                else:
                    input("수정을 취소하고 메뉴로 돌아갑니다.")  

        else:
            input("0~5번 메뉴를 선택하세요!")              


if __name__=="__main__":
    submenu()