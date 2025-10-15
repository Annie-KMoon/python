import smtplib
from account import *
from email.message import EmailMessage
import time
#한글메세지보내기

msg = EmailMessage()
msg['Subject'] = '파일첨부예제'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'mkonederland@gmail.com'
msg.set_content('파일을 첨부합니다..')

with open('manage.png', 'rb',)as file:
    msg.add_attachment(file.read(), maintype='image', subtype='png',
                       filename=file.name)

#구글 - MIME Type: 메인/서브타입 체크 가능
with open('sample.xlsx', 'rb',)as file:
    msg.add_attachment(file.read(), maintype='application', subtype='octet-stream',
                       filename=file.name)

with smtplib.SMTP('smtp.gamil.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, APP_PASSWORD)
    time.sleep(3)

    msg = EmailMessage()
    msg['Subject'] = '파일첨부예제'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'mkonederland@gmail.com'
    msg.set_content('파일을 첨부합니다..')
    smtp.send_message(msg)