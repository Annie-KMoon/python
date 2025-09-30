#일반가격
def price(people):
    print(f"{people}명의 가격은 총 {people * 15000:,}원 입니다.")

#조조할인
def price_morning(people):
    print(f"{people}명의 조조할인 가격은 총 {people * 10000:,}원 입니다.")

#군인할인
def price_soldier(people):
    print(f"{people}명의 군인할인 가격은 총 {people * 4000:,}원 입니다.")

if __name__=='__main__':
    price_soldier(3)
    