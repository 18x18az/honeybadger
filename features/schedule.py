from connection.mqtt import MqttClient
from workQueue import add_function
from reader.matches.getMatches import getMatches
import requests

def getScheduleHandler(server, port):
    schedule = getMatches('2')

    payload = {
        'blocks': schedule
    }

    url = f'http://{server}:{port}/api/qualSchedule'
    # print(url)

    requests.post(url, json=payload)

class ScheduleHandler(MqttClient):
    def __init__(self, server, api_port):
        self.api_port = api_port
        topics = ['inspection/canConclude', 'eventStage']
        self.tmNeedsSchedule = False
        self.canConclude = False
        super().__init__(server, topics)

    def onMessage(self, topic, payload):
        if topic == 'eventStage' and payload == 'CHECKIN':
            print('TM is waiting for schedule')
            self.tmNeedsSchedule = True
        elif topic == 'inspection/canConclude' and payload == 'true':
            print('Inspection can conclude')
            self.canConclude = True

        if self.tmNeedsSchedule and self.canConclude:
            getScheduleHandler(self.server, self.api_port)
            # print('Maestro stage is SETUP, getting teams')
            # add_function(getScheduleHandler, self.server, self.api_port)
