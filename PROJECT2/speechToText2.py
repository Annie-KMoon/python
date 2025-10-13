#연속적으로 듣기
import speech_recognition as sr
import os

def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        if '종료' in text:
            stop(wait_for_stop=False) #마이크종료
            os._exit(0) #프로그램종료
        print('[홍길동]'+text)
    except sr.UnknownValueError:
        print("인식 실패")
    except sr.RequestError:
        print("요청 실패")

print("듣고있습니다.")
mic = sr.Microphone()
stop = sr.Recognizer().listen_in_background(mic, listen) #백에서 계속 듣기

#프로그램 무한 실행
while True:
    pass