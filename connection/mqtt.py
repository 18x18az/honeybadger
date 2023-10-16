import paho.mqtt.client as mqtt
import threading

class MqttClient:
    def __init__(self, server, topics):
        self.topics = topics
        self.client = mqtt.Client(transport='websockets')
        self.client.on_message = self._onMessage
        self.client.on_connect = self._onConnect

        self.client.connect(server, 1883, 60)
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

        self.server = server

    def _onConnect(self, client, userdata, flags, rc):
        for topic in self.topics:
            self.client.subscribe(topic)

    def _onMessage(self, client, userdata, message):
        topic = message.topic
        payload = message.payload.decode('utf-8')
        self.onMessage(topic, payload)

    def onMessage(self, topic, payload):
        pass

    def _run(self):
        self.client.loop_forever()
