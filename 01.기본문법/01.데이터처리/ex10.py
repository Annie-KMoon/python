#문자열 함수
jumin='990120-2155013'

#남자?여자?
gender=jumin[7] #인덱스7의 한문자 출력
result=gender=='1'or gender=='3'
print(f'{gender} 결과는 {result}')

yy=jumin[0:2] #인덱스 0~2 전까지 출력 주의,0생략가능(0~1)
print(yy)

mm=jumin[2:4] #인덱스 2~4전까지 출력(2~3)
print(mm)

dd=jumin[4:6] #인덱스 4~6전까지 출력(4~5)
print(dd)

yymmdd=jumin[0:6] #인덱스0~6전까지 출력(0~5)
print(yymmdd)

print(f'{yy}년{mm}월{dd}일')

print(jumin[-7:]) #인덱스의 끝에서부터 6자리까지 출력(-6~)
print(jumin[-1])

