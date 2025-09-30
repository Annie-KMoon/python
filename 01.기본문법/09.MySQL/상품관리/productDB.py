#상품관리 DB
from DB import*
from classes import*


def product_list():
    try:
        sql = 'select * from product'
        cur.execute(sql)
        rows = cur.fetchall()
        products = []
        for row in rows:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']
            products.append(product)
        return products

    except Exception as err:
        print("상품목록오류:",err)
        
#숫자 입력 함수
def inputNum(title):
    while True:
        str = input(title)
        if str.isnumeric():
            return int(str)
        elif str == "":
            return str #return, break로 빠져나옴
        else:
            print("숫자로 입력하세요!")

#상품등록 함수
def insert(product):
    try:
        sql = 'insert into product(code, name, price) values(%s,%s,%s)'
        cur.execute(sql, (product.code, product.name, product.price))
        con.commit()
        print("상품등록성공!")
    except Exception as err:
        print("상품등록오류:",err)

#상품검색 함수
def search(value):
    try:
        sql = 'select * from product where code like %s or name like %s'
        value = f'%{value}%'
        cur.execute(sql, (value,value,))
        rows = cur.fetchall()
        if rows != None:
            products = []
            for row in rows:
                product = Product()
                product.code = row['code']
                product.name = row['name']
                product.price = row['price']
                products.append(product)
            return products

    except Exception as err:
        print("상품검색오류:",err)

#수정함수
def update(product):
    try:
        sql = 'update product set name=%s, price=%s where code =%s'
        cur.execute(sql, (product.name, product.price, product.code,))
        con.commit()
        print("상품수정완료!")

    except Exception as err:
        print("상품정보수정오류:", err)

#읽기함수
def read(code):
    try:
        sql = 'select * from product where code =%s '
        cur.execute(sql,(code))
        row =cur.fetchone()
        if row !=None:
            product = Product()
            product.code = row['code']
            product.name = row['name']
            product.price = row['price']
            return product

    except Exception as err:
        print("상품읽기오류:",err)

#코드입력함수 메뉴-입력/수정 사용(1,4)
def inputCode(title):
    while True:
        code = input(title)
        if code=="":
            # input("메뉴로 돌아가려면 아무 키나 누르세요.")
            return code
        elif len(code) !=3:
            print("상품코드는 3자리 숫자로 입력하세요!(ex: 103)")
        elif not code.isnumeric():
            print("상품코드는 3자리 숫자로 입력하세요!(ex: 103)")
        else:
            return code

#가격입력함수
def inputPrice(title):
    while True:
        price = input(title)
        if price =="":
            return 0
        elif not price.isnumeric():
            print("가격은 숫자로 입력하세요!")
        else:
            return int(price)





#테스트
if __name__=="__main__":
    pass

    # #inputPrice test
    # price = inputPrice("상품가격>")
    # print("가격:", price)

    # #inputCode test
    # code = inputCode()
    # print("사용할수있는코드:",code)

    # #읽기 테스트
    # product = read('109')
    # if product == None:
    #     print('해당상품이 없습니다.')
    # else:
    #     product.print()

    # #검색테스트
    # products = search('10')
    # if len(products) == 0:
    #     print("검색 상품 정보가 없습니다.")
    # else:
    #     for product in products:
    #         product.print()

    # #프로덕트 등록 테스트
    # product = Product()
    # product.code = '104'
    # product.name = '엘지 TV'
    # product.price = 2150000
    # insert(product)

    #리스트 테스트
    products = product_list()
    for product in products:
        product.print()