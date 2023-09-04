from interaction.clicker import clickAt, enterText
from reader.base.clicker import hitSpace, hitTab
from reader.base.reader import getRegion


SCORE_TOP_Y = 425
SCORE_BOTTOM_Y = 455
SCORE_1_X = 413
SCORE_2_X = 759
SCORE_WIDTH = 90

BUTTON_Y = 730

SCORE_X = 400
RESET_X = 580

START_X = 280
START_Y = 200

def startInput():
    score1 = getRegion([[SCORE_1_X, SCORE_TOP_Y], [SCORE_1_X + SCORE_WIDTH, SCORE_BOTTOM_Y]])[0].text
    score2 = getRegion([[SCORE_2_X, SCORE_TOP_Y], [SCORE_2_X + SCORE_WIDTH, SCORE_BOTTOM_Y]])[0].text
    
    if score1 != '(0)' or score2 != '(0)':
        print('Appears to already have scores, resetting')
        clickAt(RESET_X, BUTTON_Y)

    clickAt(START_X, START_Y)

def inputValues(vals: list[str]):
    startInput()

    print('Inputting values')
    for val in vals:
        if val == '':
            pass
        elif val == '.':
            hitSpace()
        else:
            enterText(val)

        hitTab()
    
    print('Submitting')
    clickAt(SCORE_X, BUTTON_Y)