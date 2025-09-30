#문자열 처리함수
str='python is amazing'
print(1,str.lower()) #소문자화
print(2,str.upper()) #대문자화
print(3,str.capitalize()) #앞글자만 대문자화
print(4,str[0].islower()) #앞글자가 소문자인지 불린(t/f)
print(5,len(str)) #전체 문장의 글자수측정
print(6,str.replace('python','파이썬')) #str의 문장 대체
#특정 문자열 몇번째 인덱스열인지 값 출력
index=str.index('a')
print(index)
print(str[index:]) #찾는 문자열부터 끝까지 출력
print(str[index:].upper()) #+대문자로 출력 함수 추가(좌-우)

print(str.find('a')) #오류가 나지 않음(-1로 출력), index와 find 중에 find 사용추천

print(8,str.count('is')) #문자열 카운팅 출력
