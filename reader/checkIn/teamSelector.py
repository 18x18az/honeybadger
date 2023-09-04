from interaction.clicker import clickAt
from reader.base.reader import getRegion

SELECT_SPOT = 77

TOP_LEFT = [14, 100]
BOTTOM_RIGHT = [SELECT_SPOT, 528]

def getQualSelector():
    return getRegion([TOP_LEFT, BOTTOM_RIGHT])

def selectTeam(teams: list[str], team: str):
    print(f"Selecting team {team}")
    things = getQualSelector()
    firstIndex = None
    lastIndex = None

    for thing in things:
        if thing.text in teams:
            if not firstIndex:
                firstIndex = teams.index(thing.text), thing.y
            else:
                lastIndex = teams.index(thing.text), thing.y
    
    scale = (lastIndex[1] - firstIndex[1]) / (lastIndex[0] - firstIndex[0])
    
    index = teams.index(team)
    teamPosition = firstIndex[1] + (index - firstIndex[0]) * scale
    clickAt(SELECT_SPOT, teamPosition)
    