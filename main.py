from interactions.setup import createNew, saveTournament
from interaction.screen import getScreenComponents
from interaction.clicker import enterText

#createNew()
#saveTournament()
components = getScreenComponents()
for component in components:
    print(component.text)