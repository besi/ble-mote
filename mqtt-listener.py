import paho.mqtt.client as mqtt

host = '192.168.1.112'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("devices/ble-remote/buttons/#")


def on_message(client, userdata, msg):
    handleMessage(msg)


def handleMessage(msg):
    if 'KEY_POWER' in msg.topic:
        print('TODO: Do something on the mac')


client = mqtt.Client(client_id="", clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
client.on_connect = on_connect
client.on_message = on_message

client.connect(host)
client.loop_forever()
