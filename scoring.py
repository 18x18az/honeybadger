import math
import pyautogui
from utils import find

MATCH_HEIGHT = 16
MATCH_X = 60

upArrowLocation = None
def getUpArrow():
    global upArrowLocation
    if not upArrowLocation:
        upArrowLocation = find('upArrow')
    return upArrowLocation

downArrowLocation = None
def getDownArrow():
    global downArrowLocation
    if not downArrowLocation:
        downArrowLocation = find('downArrow')
    return downArrowLocation

screenHeight = None
def getScreenHeight():
    global screenHeight
    if not screenHeight:
        top = getUpArrow().top
        bottom = getDownArrow().top
        difference = bottom - top
        screenHeight = math.floor(difference / MATCH_HEIGHT) + 1
    return screenHeight

def selectTab():
    tabLocation = find('scoringTab')
    if tabLocation:
        print("Switching to scoring tab")
        pyautogui.click(tabLocation)

def scrollToTop():
    while not find('qualificationExpanded'):
        pyautogui.click(getUpArrow())
    print("Vertical scroll reset")

def resetForQualification():
    selectTab()
    collapsed = find('qualificationCollapsed')
    
    if collapsed:
        print("Expanding qualification matches")
        pyautogui.click(collapsed, clicks=2)
    else:
        expanded = find('qualificationExpanded')
    
        if not expanded:
            print("Scrolling up to reset vertical scroll")
            scrollToTop()

def selectQual(match):
    print(f"Selecting match {match}")
    resetForQualification()
    if(match + 1 > getScreenHeight()):
        print("Scrolling down to reach match")
        for i in range(match + 1 - getScreenHeight()):
            pyautogui.click(getDownArrow())
        match = getScreenHeight() - 1
    y = getUpArrow().top + (match + 1) * MATCH_HEIGHT
    pyautogui.click(MATCH_X, y)
    print("Match selected")

def score():
    selectQual(57)
    selectQual(60)