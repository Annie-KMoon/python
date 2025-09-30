products = [
    {'code':1, 'name':'LG 냉장고','price':2500000},
    {'code':2, 'name':'삼성 세탁기','price':1800000},
    {'code':3, 'name':'삼성 냉장고','price':2100000},
    {'code':4, 'name':'LG 전자동 세탁기','price':2000000},
]

while True:
    print('\n****************상품관리 프로그램****************')
    print('-'*50)
    print('|1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료|')
    print('-'*50)
    menu = input('메뉴 선택>')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break
    elif menu == '1':
        codes = []
        for p in products: #products에서 가져오는 것
            codes.append(p['code'])
        new_code = max(codes)+1
        print(f'상품코드>{new_code}')
        new_name = input('상품이름>')
        new_price = int(input('상품가격>')) #int로 숫자
        products.append({'code':new_code,'name':new_name,'price':new_price})
        print('새로운 상품이 등록되었습니다')
    elif menu == '2':
        for p in products:
            print(f'{p["code"]:<5}', end='\t')
            print(f'{p["name"]:<25}',end='\t')
            print(f'{p["price"]:>15,}원')
    elif menu == '3':
        search_name = input('검색할 상품이름')
        for p in products:
            if p['name'].find(search_name) != -1:
                print(p['code'], p['name'], f"{p['price']:,}원")
    elif menu == '4':
        del_code = input('삭제코드>')
        if not del_code.isnumeric(): #삭제코드 외 문자 입력시
            print('삭제코드는 숫자입니다.')
            continue
        for index, p in enumerate(products): #삭제할 번호 
            if int(del_code) == p['code']:
                products.pop(index)
                print(f'{p["name"]} 상품이 삭제되었습니다.')
    elif menu == '5':
        edit_code = input('수정코드>')
        for p in products:
            if int(edit_code) == p['code']:
                #상품이름 수정
                new_name = input(f'상품이름:{p["name"]}>')
                if new_name != '': #뉴네임에 입력값이 있을 때
                    p['name'] = new_name #상품의 새이름을 이름으로 넣는다
                #상품가격수정
                new_price = input(f'상품가격:{p["price"]:,}>')
                if new_price != '': 
                    p['price'] = int(new_price)
    else:
        print('0~5번을 다시 선택하세요')  