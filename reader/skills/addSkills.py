from interaction.clicker import clickAt, enterText
from reader.base.clicker import hitTab


TEAM_INPUT_X = 925
TEAM_INPUT_Y = 115

INPUT_X = 812
INPUT_Y = 224

DRIVE_X = 704
PROG_X = 908
SELECT_Y = 453

SAVE_X = 774
SAVE_Y = 480

def enterTeamNumber(teamNumber: str):
    clickAt(TEAM_INPUT_X, TEAM_INPUT_Y)
    enterText(teamNumber)

def enterSkillsScore(team: str, score: list[str], isProg: bool):
    enterTeamNumber(team)

    clickAt(INPUT_X, INPUT_Y)
    for input in score:
        enterText(input)
        hitTab()

    if isProg:
        clickAt(PROG_X, SELECT_Y)
    else:
        clickAt(DRIVE_X, SELECT_Y)

    clickAt(SAVE_X, SAVE_Y)
