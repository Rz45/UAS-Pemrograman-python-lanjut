import pywhatkit as w
import time
import pyautogui
import keyboard as k

pesan = """INI ADALAH TEXT OTOMATIS\nTHIS IS AUTOMATIC MESSAGE"""

w.sendwhatmsg("+6281392516787", pesan, 22,52)
pyautogui.click(1050, 950)
time.sleep(2)
k.press_and_release('enter')