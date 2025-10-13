#라이브러리 import(텍스트-음성변환/ 사운드재생)
from gtts import gTTS
from playsound import playsound

#음성저장 파일명 지정
file_name = 'data/sample.mp3'
text = 'Can I help you?'
tts_en = gTTS(text=text, lang='en') #텍스트param=text, lang=영어
tts_en.save(file_name) #파일네임으로 저장
playsound(file_name)