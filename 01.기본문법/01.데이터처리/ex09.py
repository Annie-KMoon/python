#기본함수
print(1,abs(-5)) #절대값
print(2,pow(4,3)) #함수(4의 3승)
print(3,max(5,2,10,1,7)) #최댓값
print(4,min(5,2,10,1,7)) #최솟값
print(5,round(3.14159)) #반올림
print(6,round(3.14159,3)) #반올림 소수점3자리까지 출력

from math import *
print(7,floor(4.99)) #버림
print(8,ceil(3.01)) #올림
print(9,sqrt(144)) #제곱근

from random import *
print(10, random()) #0이상 1미만 임의의 값 출력
print(11, random()*10) #0이상 10미만 임의의 값 출력
print(12, int(random()*10)) #0이상 10미만 임의의 정수 출력
print(13, int(random()*10)+1) #1이상 10이하 임의의 정수 출력

print(14,randint(1,45)) #1이상 45이하의 임의의 정수 생성
print(15,randrange(1,45)) #1이상 45미만의 임의의 정수 생성