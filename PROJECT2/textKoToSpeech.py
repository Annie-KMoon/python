#라이브러리 import(텍스트-음성변환/ 사운드재생)
from gtts import gTTS
from playsound import playsound

#음성저장 파일명 지정
file_name = 'data/sample2.mp3'
text = '파이썬을 배우면 이런 것도 할 수 있어요.'
tts_ko = gTTS(text=text, lang='ko') #텍스트param=text, lang=한국어
tts_ko.save(file_name) #파일네임으로 저장
playsound(file_name)