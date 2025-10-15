import pyautogui

pyautogui.sleep(2)
# aw = pyautogui.getActiveWindow()
# print(aw.title)
# print(aw.size)

# pyautogui.moveTo(aw.left+50, aw.top+10, duration=1)
# pyautogui.click(aw.left+50, aw.top+10, duration=1)

# for w in pyautogui.getAllWindows():
#     print(w)

windows = pyautogui.getWindowsWithTitle('제목 없음')
for w in windows:
    print(w)

w1 = windows[0]
if w1.isActive ==False:
    w1.activate()

if w1.isMaximized ==False:
    w1.maximize()

# if w1.isMinimized ==False:
#     w1.minimize()

# w1.close()