sum=0
while True:
    num = input('숫자입력>')
    if num == '': #num에 아무것도 없다면
        print('프로그램종료')
        break   #빠져나오기
    sum += int(num)
print('합계:',sum)
