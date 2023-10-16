from connection.mqtt import MqttClient
from reader.teams.getTeams import getTeams
from workQueue import add_function
import requests

def getTeamsHandler(server, port):
    teams = getTeams()

    url = f'http://{server}:{port}/api/teams'
    print(url)

    requests.post(url, json=teams)

class TeamsHandler(MqttClient):
    def __init__(self, server, port):
        topics = ['eventStage']
        super().__init__(server, topics)
        self.api_port = port

    def onMessage(self, topic, payload):
        if payload == 'SETUP':
            getTeamsHandler(self.server, self.api_port)
            print('Maestro stage is SETUP, getting teams')
            add_function(getTeamsHandler, self.server, self.api_port)
