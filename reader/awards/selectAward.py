from interaction.clicker import clickAt
from reader.base.reader import getRegion


LIST_TOP_LEFT = [14, 100]
LIST_BOTTOM_RIGHT = [210, 733]

def selectAward(selectedAward: str):
    awards = getRegion([LIST_TOP_LEFT, LIST_BOTTOM_RIGHT])
    for award in awards:
        if award.text == selectedAward:
            clickAt(award.x, award.y)
            return

    raise KeyError(f"Could not find award {award}")