from product import Product
from datetime import date #파이썬내 datetime pkg

class Sale(Product):
    def __init__(self, code, name, price, qnt):
        super().__init__(code, name, price)
        self.seq=0
        self.qnt = qnt
        self.date = date.today()
        self.sum = self.price*self.qnt

    def dict(self):
        child = super().dict()
        child['seq']=self.seq
        child['qnt']=self.qnt
        child['date']=self.date
        child['sum']=self.sum
        return child


if __name__=='__main__': #테스트
    s = Sale('001','냉장고',280,10)
    print(s.dict())