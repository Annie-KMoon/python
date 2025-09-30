file_name = "data/juso.txt"

with open(file_name,'a',encoding='utf-8') as file: #txt확장자(메모장,텍스트),'a':append, 파일생성
    name = '홍길동'
    phone = '010-1010-1010'
    address = '서울 강서구 화곡동'
    file.write(f"{name},{phone},{address}\n")

    name = '심청이'
    phone = '010-1010-2010'
    address = '인천 서구 경서동'
    file.write(f"{name},{phone},{address}\n")

#키보드 인풋-write로 파일에 저장