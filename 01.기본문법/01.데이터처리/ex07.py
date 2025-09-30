#나이, 성별 입력 받아서 여자 목욕탕 출입 가능 조건 확인
#조건: 여자 or (남자 and age<4)

print('나이와 성별을 입력하세요')
age = int(input('나이>'))
gender = input('성별>')

print('여탕에 입장 가능한가요?')
result = (gender=='여자'or(gender=='남자'and age < 4))
print(f'결과는 {result}입니다.')

print('-'*50)
print('남탕에 입장 가능한가요?')
#조건: 남자 or (여자 and age<3)
result = (gender=='남자'or(gender=='여자'and age < 3))
print(f'결과는 {result}입니다.')