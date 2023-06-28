import pyautogui
import time

def find(resource):
    location = pyautogui.locateOnScreen(f"resources/{resource}.png")
    return location

def clickIfExists(resource, clicks=1):
    location = pyautogui.locateOnScreen(f"resources/{resource}.png")
    x, y = pyautogui.center(location)
    print(x)
    pyautogui.click(x, y, clicks)