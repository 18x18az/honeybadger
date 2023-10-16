from connection.connect import get_server
from features.schedule import ScheduleHandler
from features.teams import TeamsHandler
from reader.teams.getTeams import getTeams

addr, api_port = get_server()

ScheduleHandler(addr, api_port)
TeamsHandler(addr, api_port)
