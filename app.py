
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

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")      

pyautogui.press("enter")

time.sleep(3)

# Login on the system
pyautogui.press("tab")

pyautogui.write("eliferinacio@gmail.com")

pyautogui.press("tab")

pyautogui.write("minha senha")

#pyautogui.press("tab")
pyautogui.press("tab")

pyautogui.press("enter")

# Fazer Login
# pyautogui.click()

# Import products data base
# pip install pandas openpyxl

import pandas 

tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# Sign up products

for linha in tabela.index:
    pyautogui.press("tab")

    #cod
    cod = tabela.loc[linha, "codigo"]
    pyautogui.write(str(cod))
    pyautogui.press("tab")

    #brand
    brand = tabela.loc[linha, "marca"]
    pyautogui.write(str(brand))
    pyautogui.press("tab")

    #type
    typ = tabela.loc[linha, "tipo"]
    pyautogui.write(str(typ))
    pyautogui.press("tab")

    #category
    category = tabela.loc[linha, "categoria"]
    pyautogui.write(str(category))
    pyautogui.press("tab")

    #price
    price = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(price))
    pyautogui.press("tab")

    #cust
    cust = tabela.loc[linha, "custo"]
    pyautogui.write(str(cust))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")