from connection.mqtt import MqttClient


class ScheduleHandler(MqttClient):
    def __init__(self, server):
        topics = ['inspection/canConclude']
        super().__init__(server, topics)

    def onMessage(self, topic, payload):
        print('ScheduleHandler.onMessage', topic, payload)
