file_name = "data/juso.txt" #파일 불러오기
try:
    with open(file_name, 'r', encoding='utf-8') as file: #'r':read, as로 별명화
        lines = file.readlines() #lines: 전체읽기
        #print(lines, type(lines),len(lines))
        for line in lines:
            # print(line, end="") #데이터 한줄씩 출력
            items = line.split(",") #데이터값 분리 (사이에 ,),배열변동 idx0부터~
            print(f"이름:{items[0]}, 전화:{items[1]}, 주소:{items[2]}", end="")

except Exception as err:
    print("주소파일을 찾을 수 없습니다.",err)