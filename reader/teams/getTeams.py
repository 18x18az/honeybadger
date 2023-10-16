from interaction.readCsv import readCsv
from reader.fileMenu.fileMenu import export

def getTeams():
    export(1)
    csv = readCsv('TeamList.csv')
    teams = []
    for rawTeam in csv[1:]:
        team = {
            "number": rawTeam[0],
            "name": rawTeam[1],
            "city": rawTeam[2],
            "state": rawTeam[3],
            "country": rawTeam[4],
            "ageGroup": rawTeam[8],
        }
        print(team)
        teams.append(team)

    return teams