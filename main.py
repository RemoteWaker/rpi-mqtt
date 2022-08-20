from paho.mqtt.client import Client
from paho.mqtt.client import MQTTMessage
import os
from wakeonlan import send_magic_packet

device_id = os.getenv("BALENA_DEVICE_UUID")


def on_connect(client: Client, userdata, flags, rc):
    print("connected with result code:" + str(rc))

    client.subscribe("remotewaker/" + device_id)


def on_message(client, userdata, msg: MQTTMessage):
    payload = str(msg.payload)
    splitted = payload.split(',')
    computer_mac = splitted[1].split(':')[1]
    send_magic_packet(computer_mac)


client = Client(client_id=device_id, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.connect("vicart.dev", 1883)

client.loop_forever()
