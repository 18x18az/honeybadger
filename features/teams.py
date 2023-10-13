from connection.mqtt import MqttClient
from reader.teams.getTeams import getTeams


class TeamsHandler(MqttClient):
    def __init__(self, server):
        topics = ['eventStage']
        super().__init__(server, topics)

    def onMessage(self, topic, payload):
        if payload == 'SETUP':
            teams = getTeams()
            print(teams)
