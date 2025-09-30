#list 타입 -여러개 데이터 저장
names=['홍길동','심청이','강감찬']
print(names,type(names))

names.append('박명수') #추가데이터
print(names,type(names))

names.pop() #최근데이터 제외
print(names)

names.insert(1,'박명수') #인덱스1순서에 데이터 추가
names.append('박명수')
print(names)

print(names.count('박명수')) #데이터 카운팅
print(names, names[-2:]) #뒤에서 두 인덱스 출력
print(names, names[1:3]) #원하는 인덱스 위치 출력