from interaction.clicker import clickAt
from reader.base.clicker import hitEnter, hitSpace, hitTab
from reader.base.reader import awaitText, awaitTextGone, getRegion
import time

from reader.base.tabSelect import resetTab


TOOLS_X = 130
TOOLBAR_Y = 30

DROPDOWN_TOP_LEFT = [110, 48]
DROPDOWN_BOTTOM_RIGHT = [350, 270]

WELCOME_TOP_LEFT = [250, 45]
WELCOME_BOTTOM_RIGHT = [400, 90]

POPUP_TOP_LEFT = [267, 344]
POPUP_BOTTOM_RIGHT = [800, 374]

MATCH_CONTROL_TOP_LEFT = [240, 140]
MATCH_CONTROL_BOTTOM_RIGHT = [400, 170]



def regenerateSchedule():
    print('Regenerating schedule')
    clickAt(TOOLS_X, TOOLBAR_Y)
    options = getRegion([DROPDOWN_TOP_LEFT, DROPDOWN_BOTTOM_RIGHT])

    for option in options:
        if 'regenerate' in option.text:
            clickAt(option.x, option.y) # Open menu
            print('Waiting for menu to open')
            awaitText([WELCOME_TOP_LEFT, WELCOME_BOTTOM_RIGHT], 'welcome', 5)
            hitSpace() #  Don't save backup
            hitTab()
            hitTab() # Select 'next
            hitEnter()
            hitEnter() # Go to create matches
            print("Regenerating matches")
            hitEnter() # Create matches
            time.sleep(0.1)
            awaitTextGone([WELCOME_TOP_LEFT, WELCOME_BOTTOM_RIGHT], 'wait while')
            print('Matches regenerated')
            time.sleep(1)
            hitTab()
            hitTab()
            hitEnter()
            hitEnter()
            print("Waiting for TM restart")
            awaitText([MATCH_CONTROL_TOP_LEFT, MATCH_CONTROL_BOTTOM_RIGHT], 'start match', 5)
            print('Closing field control popup')
            clickAt(630, 13)
            print('Finished regenerating schedule')
            resetTab()
            return