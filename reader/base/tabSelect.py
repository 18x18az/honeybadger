from interaction.clicker import clickAt


currentTab = None

TAB_Y = 60

SCORE_X = 30
TEAM_X = 170
ALLIANCE_X = 254
SKILLS_X = 400
AWARDS_X = 554

def scoringTab():
    global currentTab
    if currentTab != 'scoring':
        clickAt(SCORE_X, TAB_Y)
        currentTab = 'scoring'

def teamTab():
    global currentTab
    if currentTab != 'team':
        clickAt(TEAM_X, TAB_Y)
        currentTab = 'team'

def allianceTab():
    global currentTab
    if currentTab != 'alliance':
        clickAt(ALLIANCE_X, TAB_Y)
        currentTab = 'alliance'

def skillsTab():
    global currentTab
    if currentTab != 'skills':
        clickAt(SKILLS_X, TAB_Y)
        currentTab = 'skills'

def awardsTab():
    global currentTab
    if currentTab != 'awards':
        clickAt(AWARDS_X, TAB_Y)
        currentTab = 'awards'
