class Product:
    def __init__(self, code, name, price): #객체생성자
        self.code = code
        self.name = name
        self.price = price

    def dict(self): #매서드
        return{'code':self.code, 'name':self.name, 'price':self.price}
    

if __name__== '__main__':
    p = Product('P01','냉장고', 250) #객체생성
    print(p.dict()) #dict값 출력
