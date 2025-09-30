import os

path = os.getcwd() #현재경로확인
print('현재폴더',path)

check = path + '/travel' #경로체크, /:경로연결부오탈자주의
if os.path.exists(check):
    os.rmdir(check) #폴더삭제
    print("폴더삭제")
else:
    os.makedirs(check) #폴더생성
    print("폴더생성")
