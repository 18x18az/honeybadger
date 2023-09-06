from interaction.clicker import clickAt
from reader.base.reader import getRegion
from reader.base.tabSelect import teamTab
from reader.checkIn.teamSelector import selectTeam

checkBoxTopLeft = [1126, 400]
checkBoxBottomRight = [1140, 410]

saveX = 1095
saveY = 446

def checkIn(teams: list[str], team: str, present: bool):
    teamTab()
    selectTeam(teams, team)
    current = getRegion([checkBoxTopLeft, checkBoxBottomRight])
    
    if (len(current) == 1) != present:
        print(f"Marking team {team} as {'present' if present else 'absent'}")
        clickAt(1133, 405)
        clickAt(saveX, saveY)
    else:
        print(f"Team {team} already marked as {'present' if present else 'absent'}")