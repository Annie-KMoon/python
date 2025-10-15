import pyautogui

# pyautogui.sleep(3)
# p = pyautogui.position()
# print(p)

# pyautogui.sleep(2)
# pyautogui.moveTo(140,65, duration=1)#절대위치 이동
# pyautogui.click(129,129, duration=1)#해당위치 클릭

# pyautogui.mouseInfo() #현재위치정보등 체크가능

# pyautogui.sleep(2)
# print(pyautogui.position())
# pyautogui.moveTo(25,25, duration=0.5)
# pyautogui.move(100,100, duration=0.5) #현재위치에서 100,100으로 상대적 이동
# pyautogui.move(100,100, duration=0.5)


#메모장 선택-드래그

# pyautogui.sleep(2)
# p = pyautogui.position()
# pyautogui.moveTo(p.x, p.y, duration=0.5)
# pyautogui.drag(100,100, duration=0.5) #to-절대위치

#현재포지션 클릭
# pyautogui.sleep(2)
# p = pyautogui.position()
# pyautogui.click(p.x, p.y)

#이미지를 찾아 클릭

pyautogui.sleep(2)
try:
    manage = pyautogui.locateOnScreen('data/manage.png')
    print(manage)
except Exception:
    print("찾지 못함")
