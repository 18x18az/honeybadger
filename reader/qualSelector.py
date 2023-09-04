from interaction.screen import ScreenItem
from reader.base import getRegion
from reader.clicker import clickAt

TOP_LEFT = [46, 79]
BOTTOM_RIGHT = [170, 748]

EXPAND_X = 20
SELECT_X = 90

mostRecent = None

def lineParser(text):
    if text == 'o':
        return ''
    
    if text == 'matcr':
        return 'match'
    
    if text.startswith('oqual'):
        text = 'qual'

    text = text.replace('oau', 'qu')

    return text

def phraseParser(text: str):
    if 'qual' in text:
        text = 'qual' + text.split('qual', maxsplit=1)[1]

    if text.endswith('a'):
        text = text[:-1] + '8'

    if text == 'quali8':
        text = 'qual 18'
    
    return text

def getQualSelector():
    return getRegion([TOP_LEFT, BOTTOM_RIGHT], lineParser, phraseParser)

def selectQual(qual: int):
    items = getQualSelector()
    numItems = len(items)
    if numItems == 3 or numItems == 4:
        if all(item.text in ['practice', 'qualification', 'elimination', 'field test match'] for item in items):
            print('Not expanded, attempting to expand')
            for item in items:
                if item.text == 'qualification':
                    print('Expanding qualification tab')
                    clickAt(EXPAND_X, item.y)
                    return selectQual(qual)
            print('Qual not found, it must be highlighted, clicking elsewhere')
            clickAt(SELECT_X, items[0].y)
            return selectQual(qual)
        
    firstDataPoint = None
    lastDataPoint = None
    for item in items:
        
        try:
            if not item.text.startswith('qual '):
                continue

            number = int(item.text.split('qual ')[1])
            if not firstDataPoint:
                firstDataPoint = (number, item)
            else:
                lastDataPoint = (number, item)
        except IndexError:
            continue
        except ValueError:
            continue

    if not lastDataPoint:
            raise ValueError(f'Could not infer location')
        
    difference = lastDataPoint[0] - firstDataPoint[0]
    differenceY = lastDataPoint[1].y - firstDataPoint[1].y
    scale = differenceY / difference
    desiredQualY = firstDataPoint[1].y + (scale * (qual - firstDataPoint[0]))
    print(f"Selecting qual {qual}")
    clickAt(SELECT_X, desiredQualY)
            