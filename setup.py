from utils import find
import time
import pyautogui

def closeFieldControl():
    print("Making sure no field control windows are open")
    fieldControl = find('fieldcontrol')
    if(fieldControl):
        print("Field control window found, closing")
        close = find('closeControl')
        pyautogui.click(close)

def openExisting():
    print("Loading existing TM file")
    existingButton = find('existing')
    pyautogui.click(existingButton)
    time.sleep(1)
    print("Navigating to folder")
    filepath = find('filepath')
    pyautogui.click(filepath)
    pyautogui.press('backspace')
    pyautogui.typewrite('C:\\Users\\Alec\\Documents\\TestFolder')
    pyautogui.press('enter')
    time.sleep(1)
    print("Opening file")
    existingFile = find('tmfile')
    pyautogui.click(existingFile, clicks=2)
    print("Waiting for TM to load")
    time.sleep(10)
    closeFieldControl()

def ensureOpen():
    print("Starting TM")
    pyautogui.press('win')
    pyautogui.typewrite('tournament manager')
    pyautogui.press('enter')
    time.sleep(5)

    updatePostpone = find('update')
    if updatePostpone:
        print("Postponing update")
        pyautogui.click(updatePostpone)
        time.sleep(3)

    openExisting()

def ensureVisible():
    taskbarLocation = find('logo')

    if not taskbarLocation:
        print("TM is not currently open")
        ensureOpen()
    else:
        print("TM is minimized, opening")
        pyautogui.click(taskbarLocation, clicks=2)

def setup():
    print("Setting up window layout")
    leftHeaderPos = find('headerLeft')

    if not leftHeaderPos:
        print("TM is not currently maximized on the screen")
        ensureVisible()
        time.sleep(0.5)
        leftHeaderPos = find('headerLeftFocus')

    pyautogui.click(leftHeaderPos.left, leftHeaderPos.top)

    if leftHeaderPos.left > 10 or leftHeaderPos.top > 10:
        print("Positioning TM to the left of the screen")
        with pyautogui.hold('win'):
            pyautogui.press('left')
            
    print("Finished setup")