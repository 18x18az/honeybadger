from interaction.readCsv import readCsv
from reader.fileMenu.fileMenu import export
import datetime
import time

def normalizeTime(localTime):
    zuluTime = localTime + datetime.timedelta(seconds=time.timezone)
    formattedTime = zuluTime.isoformat() + 'Z'
    return formattedTime

def makeBlock(matches, startTime, endTime):
    return {
        'start': normalizeTime(startTime),
        'cycleTime': (endTime - startTime).total_seconds() / (len(matches) - 1),
        'matches': matches
    }

def getMatches(round):
    export(2)
    csv = readCsv('Matches.csv')
    blocks = []
    blockStartTime = None
    currentBlock = None
    previousTime = None
    for rawMatch in csv[1:]:
        if rawMatch[1] != round:
            continue

        if currentBlock and len(currentBlock) == 1:
            blockStartTime = previousTime

        rawTime = rawMatch[17]
        localTime = datetime.datetime.strptime(rawTime, '%Y-%m-%d %H:%M:%S')

        match = {
            "number": int(rawMatch[3]),
            "redAlliance": {
                "team1": rawMatch[5],
                "team2": rawMatch[6]
            },
            "blueAlliance": {
                "team1": rawMatch[8],
                "team2": rawMatch[9]
            }
        }

        if previousTime:
            # Time delta in seconds
            timeDelta = (localTime - previousTime).total_seconds()
        
        if not previousTime or timeDelta > 1620:
            if currentBlock:
                block = makeBlock(currentBlock, blockStartTime, previousTime)
                blocks.append(block)

            currentBlock = []

        previousTime = localTime
        currentBlock.append(match)

    block = makeBlock(currentBlock, blockStartTime, previousTime)
    blocks.append(block)
    return blocks

def getQualMatches():
    return getMatches('2')
