#오늘의 환율 물을때 답변해주는 AI 스피커
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from scraping import weather, exchange, stock #answer.py에서 import

#문자를 소리로 출력 함수(gtts)
def speak(text):
    print("[인공지능]"+text)
    tts = gTTS(text=text, lang='ko')
    file_name = 'data/voice.mp3'
    tts.save(file_name)
    playsound(file_name)
    #voice 생성파일삭제
    if os.path.exists(file_name):
        os.remove(file_name)

#음성 청취 후 문자 변환
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        answer(text)
        # if '종료' in text:
        #     stop(wait_for_stop=False) #마이크종료
        #     os._exit(0) #프로그램종료
        # print('[홍길동]'+text)
    except sr.UnknownValueError:
        print("인식 실패")
    except sr.RequestError:
        print("요청 실패")

#문자입력 받아서 인공지능 대답
def answer(text):
    answer_text=''
    if '종료' in text:
        answer_text = '다음에 또 만나요.'
        speak(answer_text)
        stop(wait_for_stop=False)
        os._exit(0)
    elif '안녕' in text:
        answer_text='안녕하세요! 반갑습니다.'
    elif '날씨' in text:
        index = text.find('날씨')
        query = text[:index +2]
        temp=weather(query)
        answer_text = f'{query}의 기온은 {temp}입니다.'
    elif '환율' in text:
        rate = exchange()
        answer_text='1달러 환율은 '+rate+'원 입니다.'
    elif '주식' in text:
        index = text.find('주식')
        query = text[:index +2]
        price = stock(query)
        answer_text = f'{query}의 가격은 {price}입니다.'
    else:
        answer_text= '잘 모르겠습니다. 다시 한번 말씀해주세요.'
    speak(answer_text)




#프로그램 실행
speak("무엇을 도와드릴까요?")
mic = sr.Microphone()
stop = sr.Recognizer().listen_in_background(mic, listen) #백에서 계속 듣기

#프로그램 무한 실행
while True:
    pass