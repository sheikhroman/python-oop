import pyautogui
import time
# pyautogui.alert('This is an alert box.')
time.sleep(3)
for i in range(1,5):
    time.sleep(3)
    pyautogui.write('Sheikh Roman', interval=0.25)
    pyautogui.press('enter')
