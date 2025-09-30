#숫자 체크 함수 / 숫자면 T, else F
def isNumber(str):
    if str.isnumeric():
        return True
    else:
        print("숫자를 입력하세요!")
        return False
    
#학점구하기 함수
def grade (score):
    grade = ""
    if score >=90:
        grade="A"
    elif score >=80:
        grade="B"
    elif score >=70:
        grade="C"
    elif score >=60:
        grade="D"
    else:
        grade="F"
    return grade

#입력 함수
def inputNum(title):
    while True:
        str = input(f"{title}>")
        if str.isnumeric(): #숫자로
            return int(str)
        elif str == "": #엔터키일때 0으로
            return 0
        else: #숫자가 아닌 문자 입력시
            print(f"{title}을(를)숫자를 입력하세요!")


#메뉴출력프로그램
def menuPrint(title):
    print(f"\n*******************{title}*******************")
    print("-"*55)
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|")
    print("-"*55)