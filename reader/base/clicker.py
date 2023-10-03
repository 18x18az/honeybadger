import pyautogui
from interaction.representation import getPosition

def hitTab():
    pyautogui.press('tab')

def hitSpace():
    pyautogui.press('space')

def hitEnter():
    pyautogui.press('enter')

def hitDown():
    pyautogui.press('down')

def hitRight():
    pyautogui.press('right')

def enterText(text: str):
    pyautogui.write(text)

def clickAt(x: int, y: int):
    pyautogui.click(x, y)

def click(text: str, partial: bool = False):
    pos = getPosition(text, partial)

    if pos:
        pyautogui.click(pos[0], pos[1])
    else:
        raise KeyError(f"Could not find {text}")