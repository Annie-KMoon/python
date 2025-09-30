import os
path = os.path.dirname(os.path.realpath(__file__))
# print("현재패스:",path)
file_name = path + "\product.txt"
# print("파일명:", file_name)

#제품 관리 클래스 설정
class Product:
    def __init__(self):
        self.code = 0
        self.name = ""
        self.price = 0
    def print(self):
        print(f"상품번:{self.code},상품명:{self.name[:20]},상품가격:{self.price:,}원") #명령어주의
        print("-"*70)

#데이터 하나 추가 함수
def fileAppend(p): #product 객체 변수 p
    with open (file_name, 'a', encoding = 'utf-8') as file:
        file.write(f"{p.code},{p.name},{p.price}\n")

#데이터 모든데이터를 다시쓰기(덮어쓰기) 함수
def fileWrite(list): #list 다시쓰기 위한 모든데이터 > 모두 반복해서 수정
    with open (file_name, 'w', encoding = 'utf-8') as file: #w 주의
        for p in list:
            file.write(f"{p.code},{p.name},{p.price}\n")

#수정함수
def update():
    code=1
    list = fileRead()
    result = [p for p in list if p.code ==code]
    p = result[0]
    p.name = "아무개"
    p.price = 560
    fileWrite(list) #1번이 아무개로 변경

#삭제함수
def delete(code):
    list = fileRead()
    result = [p for p in list if p.code !=code] #같은 코드가 아닌 것만 result
    fileWrite(result) #삭제함수(삭제번호input, 확인)
    

#모든 데이터 읽기 함수
def fileRead():
    with open (file_name, 'r', encoding = 'utf-8') as file:
        list = [] #읽어온 데이터를 리스트 변수
        lines = file.readlines() #리스트를 한줄씩 전체 조회
        for line in lines:
            items = line.split(",") #라인의 split값을 아이템으로[]
            p = Product() #이 값을 객체로 만들어 리스트로 in
            p.code = int(items[0]) #정수로 변경
            p.name = items[1]
            p.price = int(items[2].replace('\n','')) #정수로 변경
            list.append(p) #리스트로 반복된 p값 in
        return list #리스트로 리턴(for문 외부에서*)

#fileRead를 사용한 리스트 함수
def list():
    list = fileRead()
    for p in list:
        p.print()

def append(): #파일추가함수
    p = Product()
    p.code = 2
    p.name = "세탁기"
    p.price = 500
    fileAppend(p)
    print("등록성공")

#본 파일에서만 테스트
if __name__ == '__main__':
    # append() #파일추가명령어 테스트
    # list() #리스트 읽기 함수 테스트
    # delete(6) #삭제함수 테스트
    # update() #업데이트 함수 테스트
    pass