import smtplib
from account import *
from email.message import EmailMessage
import time
#한글메세지보내기

with smtplib.SMTP('smtp.gamil.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
    time.sleep(3)

    msg = EmailMessage()
    msg['Subject'] = '테스트 제목입니다.'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content('테스트 내용입니다.')
    smtp.send_message(msg)