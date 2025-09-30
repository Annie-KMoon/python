#정규식
import re

pattern = re.compile('ca.e') #정규식
while True:
    word = input("단어>")
    if word == "":
        break

#정규식 매칭 체크 함수
    match = pattern.match(word)
    if match:
        print("일치")
    else:
        print("불일치")