from interaction.clicker import clickAt
from reader.base.clicker import hitDown, hitEnter, hitRight, hitTab


FILE_X = 15
FILE_Y = 36

def openFileMenu():
    clickAt(FILE_X, FILE_Y)

def export(index):
    openFileMenu()
    return
    hitDown()
    hitDown()
    hitRight()
    for _ in range(index):
        hitDown()
    hitEnter()
    hitTab()
    hitTab()
    hitEnter()
    hitEnter()