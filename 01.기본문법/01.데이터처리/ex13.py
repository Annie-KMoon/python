#딕셔너리 타입(키/값)
students={1:'홍길동',2:'심청이',3:'강감찬'}
print(students, type(students))
print(students.get(2)) #키가 2인값을 출력 .get 직관적
print(students[2]) #리스트2값을 출력[]사용도 가능

students[4]='박명수' #키값+추가, 같은 값에 데이터 추가시 마지막 키로 수정
print(students, type(students))

print(3 in students) #키값으로 찾기(T/F로 출력)

keys = students.keys() #키값 출력, 리스트[]로 출력
print(keys, type(keys)) #dict_keys

values = students.values() #값만 출력
print(values,type(values)) #dict_values

print('박명수' in values) #값으로 찾기(T/F로 출력)