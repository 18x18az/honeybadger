from interaction.representation import awaitOnScreen, existsOnScreen, update
from interaction.clicker import click, clickAt
import time

INITIAL_TEXT = "select an option to begin using the vex tournament manager."
SAVE_IN_TEXT = "save in"
WAIT_TEXT = "please wait while the tournament server is started"

def createNew():
    if not existsOnScreen(INITIAL_TEXT):
        raise KeyError("Not on the main screen")
    
    click("create a new tournament")

def saveTournament():

    print('waiting for save dialog')
    awaitOnScreen(SAVE_IN_TEXT, 2, partial=True)
    
    clickAt(971, 519)
    update()

    if existsOnScreen('yes', partial=True):
        print('found existing, overwriting')
        clickAt(573, 443)

    update()

    if existsOnScreen(WAIT_TEXT, partial=True):
        print('waiting for TM to start')
        while(existsOnScreen(WAIT_TEXT, partial=True)):
            update()