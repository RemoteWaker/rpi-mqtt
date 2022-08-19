from paho.mqtt.client import Client
from paho.mqtt.client import MQTTMessage
import os

device_id = os.getenv("BALENA_DEVICE_UUID")


def on_connect(client: Client, userdata, flags, rc):
    print("connected with result code:" + str(rc))

    client.subscribe("remotewaker/" + device_id)


def on_message(client, userdata, msg: MQTTMessage):
    print(msg.topic + ": " + str(msg.payload))


client = Client(client_id=device_id, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.155", 1883)

client.loop_forever()
