while True:

    try:
        num = input("숫자>")
        if num =="":
            print("종료됩니다.")
            break
        num = int(num)

    except Exception as err: #예외처리 양식
        print("숫자로 입력하세요.",err) #(err):에러메세지출력


# while True:
#     num = input("숫자>")
#     if num =="": break
#     num = int(num)