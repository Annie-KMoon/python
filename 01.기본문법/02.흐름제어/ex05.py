names= ['홍길동', '심청이', '강감찬', '이순신', '성춘향']

no=1
for name in names:
    print(f'{no}:{name}')
    no +=1 #no 숫자 +1로 증가
print('-'*50)

for index, name in enumerate(names): #index, name에 리턴되는 값
    print(f'{index+1}:{name}') #index+1, 1부터 시작
print('-'*50)

for index in range(len(names)):
    print(f'{index+1}:{names[index]}')  #9라인과 같은값도출