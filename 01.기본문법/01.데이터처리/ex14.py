#데이터 상수(정수, 실수, 문자열, 불린)
#변수(값을 저장하는 저장소)
#연산자(산술산자:+,-,*,/,%,// 관계(비교)연산자: >,>=,<,<=,==,!= 논리연산자: and, or, not)

#list
names = ['홍길동', '심청이', '강감찬']

#검색
print(1,names[0])

#입력
names.append('성춘향')
print(2,names)
names.insert(1,'유재석')
print(3,names)

#수정
names[1]='강호동'
print(4,names)

#삭제
names.pop(1) #삭제할 인덱스 넘버, 미기입시 최근 데이터부터 삭제 
print(5,names)

#데이터수
print(6,len(names)) 
print(7,names.count('심청이')) #특정값의 갯수
print(8,type(names))
    