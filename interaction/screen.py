from PIL import ImageGrab
import pyautogui
import pytesseract
import cv2
import numpy as nm
from pytesseract import Output
from typing import NamedTuple


class ScreenItem(NamedTuple):
    text: str
    x: int
    y: int

screenWidth, screenHeight = pyautogui.size()
pytesseract.pytesseract.tesseract_cmd ='tesseract'
custom_config = r'--oem 3 --psm 6 -c tessedit_char_blacklist=®|é\\/©[-_—'

def getScreenComponents() -> list[ScreenItem]:
  
    # Path of tesseract executable
    cap = ImageGrab.grab(bbox=(0, 0, screenWidth, screenHeight))
    gray = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)

    teststr = pytesseract.image_to_data(gray, config=custom_config, lang='eng', output_type=Output.DICT)
    
    n_boxes = len(teststr['level'])

    lines = {}
 
    # Extract and draw rectangles for all bounding boxes
    for i in range(n_boxes):
        # Add to existing line or create a new line
        lineNum = teststr['line_num'][i]
        text = teststr['text'][i].lower().strip()

        if(text == ''):
            continue
        
        x_pos = teststr['left'][i] + teststr['width'][i] / 2
        y_pos = round(teststr['top'][i] + teststr['height'][i] / 2)

        if text.startswith('(e,'):
            text = text[2:]

        if text.startswith(','):
            text = text[1:]

        if text == 'ta':
            text = 'to'
        elif text == 'fle':
            text = 'file'
        elif text == 'fles' or text == 'fes':
            text = 'files'
        elif text == "©":
            continue
        elif text == 'toumament' or text == 'tounanent':
            text = 'tournament'
        elif text == 'cancl':
            text = 'cancel'
        elif text == 'savein:':
            text = 'save in:'
        elif text == 'menage':
            text = 'manager'

        if lineNum in lines:
            lines[lineNum]["text"] += ' ' + text
            lines[lineNum]["x"].append(x_pos)
        else:
            lines[lineNum] = {"text": text, "x": [x_pos], "y": y_pos}

    # Average out x positions and round to whole number
    for key in lines:
        lines[key]["x"] = round(sum(lines[key]["x"]) / len(lines[key]["x"]))
    
    returnList = []
    for key in lines:
        returnList.append(ScreenItem(lines[key]["text"], lines[key]["x"], lines[key]["y"]))

    return returnList
