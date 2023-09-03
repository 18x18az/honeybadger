from interaction.screen import getScreenComponents, ScreenItem
import time

current: list[ScreenItem] | None= None

def update():
    global current
    current = getScreenComponents()

def getPosition(text: str, partial: bool = False) -> tuple[int, int] | None:
    match = getMatch(text, partial)

    return (match.x, match.y) if match else None

def getMatch(text: str, partial: bool) -> ScreenItem | None:
    if not current:
        update()

    text = text.lower()

    for item in current:
        if partial:
            if text in item.text:
                return item
        else:
            if text == item.text:
                return item
            
    return None

def existsOnScreen(text: str, partial: bool = False) -> bool:
    return getMatch(text, partial) is not None

def awaitOnScreen(text: str, timeout: int, partial: bool = False):
    startTimer = time.time()
    endTime = startTimer + timeout
    update()
    while not existsOnScreen(text, partial):
        update()
        if time.time() > endTime:
            raise TimeoutError(f"Timed out waiting for {text}")