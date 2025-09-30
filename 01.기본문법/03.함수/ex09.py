#숫자가 입력될 때 까지 계속 입력하는 함수

def inputNum(title):
    while True: #반복/ True 사이에 조건식 가능
        num = input(f"{title}>")
        if num.isnumeric(): #숫자인지 판별하는 isnumeric
            return int(num) #숫자로 데이터값 돌려줌
        elif num == "": #blank 입력시
            return num
        else:
            print("숫자로 입력하세요!")

num = inputNum("숫자입력")
print(num, type(num))


#검색 함수: list와 코드를 입력받아서 list에서 code를 검색하는 함수

def search(list, code): #N개이상 기입시 ,
    for index, item in enumerate(list): #list에서 item으로
        if item['code']==code: #index번호찾기-enumerate key=code로 통일
            return index
        
sale = [
    {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
    {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
]

index = search(sale,1)
if index == None:
    print("해당 데이터가 없습니다.")
else:
    print(sale[index])
