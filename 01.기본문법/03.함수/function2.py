#숫자가 입력될 때 까지 계속 입력하는 함수
def inputNum(title):
    while True: #반복/ True 사이에 조건식 가능
        num = input(f"{title}")
        if num.isnumeric(): #숫자인지 판별하는 isnumeric
            return int(num) #숫자로 데이터값 돌려줌
        elif num == "": #blank 입력시
            return num
        else:
            print("숫자로 입력하세요!")

#검색 함수: list와 코드를 입력받아서 list에서 code를 검색하는 함수

def search(list, code): #N개이상 기입시 ,
    for index, item in enumerate(list): #list에서 item으로
        if item['code']==code: #index번호찾기-enumerate key=code로 통일
            return index
        
#메뉴출력프로그램
def menuPrint(title):
    print(f"\n*******************{title}*******************")
    print("----------------------------------------------")
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|")
    print("----------------------------------------------")

#새로운 코드 생성 함수
def newCode(list):
    if len(list) == 0:
        return 1
    else:
        codes = []
        for s in list:
            codes.append(s['code'])
        return max(codes)+1
    
#아이템 출력 함수
def itemPrint(item): #다른 리스트에서 동일하게 쓰려면 key값을 구해야함
    keys= item.keys()
    for key in keys:
        if isinstance(item[key], int): #isinstance(정수인지확인식)
            print(f"{item[key]:,}", end="\t")
        else:
            print(f"{item[key]:<10}", end="\t")
    print()
    print('-'*50)

#다른 파일에 import시 실행하고 싶지 않을 때
if __name__=='__main__':

    sale = [
        {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
        {'code':2, 'name':'세탁기', 'price':1500000, 'qnt':3},
]

    itemPrint(sale[1])
