from function import *
from sale import Sale

products =[
    {'code':'001', 'name':'LG 냉장고', 'price': 250},
    {'code':'002', 'name':'LG 세탁기', 'price': 180},
]

sale = []

def search(code):
    for p in products: #리스트
        if code ==p['code']:
            return p #dict
        
def max_seq():
    seqs = []
    for s in sale:
        seqs.append(s['seq'])
    if len(seqs)==0:
        return 0
    else:
        return max(seqs)

while True:
    menuPrint("매출관리")
    menu = input("메뉴선택>")
    if menu == "0":
        print("프로그램이 종료됩니다.")
        break

    elif menu == "1": #입력
        code = input("상품코드")
        if code =="": continue
        p = search(code)
        if p == None:
            print(f"{code}번 상품이 없습니다.")
        else:
            name = p['name']
            price = p['price']
            print(f'상품명:{name}, 가격:{price}')
            qnt = inputNum("판매수량>")
            if qnt == "": continue
            s = Sale(code, name, price, qnt) #세일 클래스 만들기
            s.seq = max_seq()+1
            sale.append(s.dict()) #S는 오브젝트> 딕트로 변경
            print("매출등록완료!")

    elif menu == "2": #검색
        name = input("검색이름>")
        isFind = False #불린은 is로 변수
        for s in sale:
            if s['name'].upper().find(name.upper()) !=-1:
                print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원",end="")
                print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
                isFind = True #값 찾음
        if isFind==False: #not붙여도됨
            print("검색이름이 없습니다.")

    

    #검색이름이 없을때?/컬리-유사검색어, 오탈자도 연결, 다른플랫폼은 동일단어만 출력>이런건 어떻게?              

    elif menu == "3": #목록
        for s in sale: #S는 오브젝트> 딕트로 변경
            print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원",end="")
            print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")

    elif menu == "4": #삭제 / 같은 제품 다른 내용> seq값 설정으로 삭제
        seq = inputNum("삭제번호>")
        if seq == "": 
            print("메뉴로 돌아갑니다.")
            continue #삭제취소
        for idx, s in enumerate(sale):
            if s['seq']==seq:
                 print(f"{s['seq']},{s['code']},{s['name']},{s['price']:,}만원",end="")
                 print(f"{s['qnt']:,}개,{s['sum']:,}만원,{s['date']}")
                 sel = input("삭제하시겠습니까?(Y/N)")
                 if sel == "Y" or sel == "y":
                     sale.pop(idx) #괄호주의
                     print("매출정보삭제완료")
                 else:
                     print("메뉴로 돌아갑니다.")
                     continue

    elif menu == "5": #수정
        seq = inputNum("수정번호>")
        if seq == "": 
            print("메뉴로 돌아갑니다.")
            continue #수정취소
        for s in sale:
            if seq == s['seq']:
                print(f"상품코드:{s['code']}")
                print(f"상품이름:{s['name']}")
                print(f"판매일자:{s['date']}")
                qnt = inputNum(f"판매수량:{s['qnt']}>")
                if qnt !="":s['qnt']=qnt
                print("매출수정완료!")

    else:
        print("0~5메뉴를 선택하세요!")    