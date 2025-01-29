import pyautogui 
import time

pyautogui.PAUSE = 0.8

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

pyautogui.write("https://sigauz.unizambeze.ac.mz/login.zul")

pyautogui.press("enter")

time.sleep(2)

pyautogui.press("tab")

pyautogui.write("20204061")

pyautogui.press("tab")

pyautogui.write("Carlos123#")

pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(2)

pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.press("enter")