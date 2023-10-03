from interaction.readCsv import readCsv
from reader.fileMenu.fileMenu import export
import datetime
import time

def getMatches(round):
    export(2)
    csv = readCsv('Matches.csv')
    matches = []
    for rawMatch in csv[1:]:
        if rawMatch[1] != round:
            continue
        rawTime = rawMatch[17]
        localTime = datetime.datetime.strptime(rawTime, '%Y-%m-%d %H:%M:%S')
        zuluTime = localTime + datetime.timedelta(seconds=time.timezone)
        formattedTime = zuluTime.isoformat() + 'Z'
        match = {
            "division": rawMatch[0],
            "instance": rawMatch[2],
            "matchNumber": rawMatch[3],
            "red1": rawMatch[5],
            "red2": rawMatch[6],
            "blue1": rawMatch[8],
            "blue2": rawMatch[9],
            "timeScheduled": formattedTime,
        }

        matches.append(match)

    return matches

def getQualMatches():
    return getMatches('2')
