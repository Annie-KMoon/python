#1~100 합계
tot=0
for j in range(1, 101):
    #tot=0, 내부에 정의시 i와 동일하므로 바깥에 정의
    tot +=j #tot=tot+i(동일 수식)

print(tot)

#2~100 짝수합계
sum=0
for i in range(2, 101, 2):
    sum +=i

print(sum)

#1~99 홀수합계
sum=0
for i in range(1, 100, 2):
    sum +=i

print(sum)
