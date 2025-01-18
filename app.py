
import pyautogui 
import time

# pyautogui.click -> it's used to click
# pyautogui.press -> to press
# pyautogui.write -> to write something
# pyautogui.hotkey("ctrl", "shift", "esc") -> hotkeys


pyautogui.PAUSE = 0.5     # Da uma pausa entre a execucao doss comandos


pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")


pyautogui.write("https://www.youtube.com/")

pyautogui.press("enter")

time.sleep(3)

# Fazer Login
pyautogui.click()