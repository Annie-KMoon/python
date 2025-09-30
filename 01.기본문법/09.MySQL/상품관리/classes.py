#전체 클래스 설정

class Product:
    def __init__(self):
        self.code=""
        self.name=""
        self.price=0
    def print(self):
        print(f'코드:{self.code}, 상품명:{self.name}, 상품소비자가:{self.price:,}원')

class Sale(Product): #속성만 사용, 상품소비자가, 상품실판매가 차이 있어도 OK
    def __init__(self):
        super().__init__()
        self.seq = 0
        self.date = ""
        self.qnt = 0
        self.sum = 0
        # self.sum = self.price * self.qnt

    def print(self):
        print(f'No:{self.seq},코드:{self.code}, 상품명:{self.name}')
        print(f'판매일:{self.date},판매수량:{self.qnt}개,상품판매가:{self.price:,}원, 총 매출금액:{self.sum:,}원')
        print('-'*70)


#테스트
if __name__=="__main__":
    #프로덕트 프린트 테스트
    pro = Product()
    pro.code='101'
    pro.name='냉장고'
    pro.price=1000000
    pro.print()

    
    sale = Sale()
    sale.seq = 1
    sale.code=pro.code
    sale.name=pro.name
    sale.price=990000
    sale.date='2025-08-29'
    sale.qnt = 3
    sale.print()




