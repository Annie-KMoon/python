import speech_recognition as sr

with sr.Microphone() as source:
    print('듣고있습니다.')
    audio = sr.Recognizer().listen(source)

text =sr.Recognizer().recognize_google(audio, language='ko') #온라인제공라이브러리
print(text)