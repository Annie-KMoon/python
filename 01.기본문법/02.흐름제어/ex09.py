jusos = [
    {'no':1,'name':'홍길동','juso':'서울 강서구'},
    {'no':2,'name':'강감찬','juso':'인천 서구'},
]
while True:
    print('-'*35)
    print('\t  주소관리프로그램\t')
    print('-'*35)
    print('|1.입력|2.검색|3.수정|4.삭제|0.종료|')
    print('-'*35)
    menu= input('메뉴선택>')
    if menu == '0': #종료
        print('프로그램을 종료합니다')
        break
    elif menu == '1': #입력
        no = input('번호>')
        name = input('이름>')
        juso = input('주소>')
        jusos.append({'no':no, 'name':name, 'juso':juso})
        print('등록완료')
    elif menu == '2': #검색
        for j in jusos:
            print(j.get('no'),j.get('name'),j['juso'])
        print('total',len(jusos),'명이 존재합니다.')
    elif menu == '3': #수정
        pass  
    elif menu == '4': #삭제
        pass
    else:  #이외 숫자 입력시
        print('메뉴 0~4를 입력하세요')      

#프로그램이 실행시에만 데이터가 저장되기에 파일로 저장, 데이터베이스로 저장하도록 추가 코딩