
from reader.awards.pickWinner import selectAwardWinner
from reader.awards.selectAward import selectAward
from reader.checkIn.checkin import checkIn
from reader.setup.regenerate import regenerateSchedule
from reader.skills.addSkills import enterSkillsScore

TEAM_LIST = [str(i) for i in range(1, 25)]

regenerateSchedule()