from interaction.clicker import clickAt
from reader.awards.selectAward import selectAward
from reader.base.clicker import hitEnter
from reader.base.reader import getRegion

DROPDOWN_X = 731
DROPDOWN_Y = 152

REGION_TOP_LEFT = [597, 180]
REGION_BOTTOM_RIGHT = [743, 759]

SAVE_X = 776
SAVE_Y = 340

def selectAwardWinner(award: str, winner: str, teams: list[str]):
    selectAward(award)
    clickAt(DROPDOWN_X, DROPDOWN_Y)
    choices =  getRegion([REGION_TOP_LEFT, REGION_BOTTOM_RIGHT])
    firstMatch = None
    lastMatch = None
    for choice in choices:
        if choice.text in teams:
            if not firstMatch:
                firstMatch = teams.index(choice.text), choice.y
            else:
                lastMatch = teams.index(choice.text), choice.y

    if not lastMatch:
        raise RuntimeError(f"Could not parse team list")
    
    scale = (lastMatch[1] - firstMatch[1]) / (int(lastMatch[0]) - int(firstMatch[0]))
    index = teams.index(winner)
    winnerPosition = firstMatch[1] + (index - int(firstMatch[0])) * scale
    clickAt(DROPDOWN_X, winnerPosition)

    clickAt(SAVE_X, SAVE_Y)

AUTOFILL_X = 548
AUTOFILL_Y = 414

def autoFillWinners():
    clickAt(AUTOFILL_X, AUTOFILL_Y)
    hitEnter()
