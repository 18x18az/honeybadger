import pyautogui
import pytesseract
from typing import NamedTuple
from PIL import ImageGrab
import cv2
import numpy as nm
from pytesseract import Output

screenWidth, screenHeight = pyautogui.size()

pytesseract.pytesseract.tesseract_cmd ='tesseract'
custom_config = r'--oem 3 --psm 6 -c tessedit_char_blacklist=®|é\\/©[-_—'

class ScreenItem(NamedTuple):
    text: str
    x: int
    y: int

def getRegion(box: list[list[int, int], list[int, int]] = [[0, 0],[screenWidth, screenHeight]], lineParser = None, phraseParser = None) -> list[ScreenItem]:
    x_offset = box[0][0]
    y_offset = box[0][1]
    cap = ImageGrab.grab(bbox=(box[0][0], box[0][1], box[1][0], box[1][1]))
    gray = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)

    teststr = pytesseract.image_to_data(gray, config=custom_config, lang='eng', output_type=Output.DICT)
    
    n_boxes = len(teststr['level'])

    lines = {}

    previousBlocksLength = 0
    currentBlockLength = 0
    currentBlock = 0
 
    # Extract and draw rectangles for all bounding boxes
    for i in range(n_boxes):
        # Add to existing line or create a new line

        block = teststr['par_num'][i]
        if block != currentBlock:
            currentBlock = block
            previousBlocksLength += currentBlockLength
            currentBlockLength = 0

        offset = teststr['line_num'][i]
        currentBlockLength = offset

        lineNum = offset + previousBlocksLength
        text = teststr['text'][i].lower().strip()

        text = text.strip()

        if(text == ''):
            continue
        
        x_pos = teststr['left'][i] + teststr['width'][i] / 2 + x_offset
        y_pos = round(teststr['top'][i] + teststr['height'][i] / 2) + y_offset

        if lineParser:
            text = lineParser(text)

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
        lineText = lines[key]["text"].strip()
        if phraseParser:
            lineText = phraseParser(lineText)

        returnList.append(ScreenItem(lineText, lines[key]["x"], lines[key]["y"]))

    return returnList