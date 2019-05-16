import json

import evdev
import paho.mqtt.publish as publish

device = evdev.InputDevice('/dev/input/event1')
print(device)

down = 1
up = 0
hold = 2

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.value == down:
        # print(evdev.categorize(event))
        key = evdev.ecodes.KEY[event.code]

        # The mute key is special since it will produce an array of keys
        if event.code == 113: key = 'KEY_MUTE'
        print(key)
        payload = json.dumps({
            "sec": event.sec,
            "usec": event.usec,
            "code": event.code,
            "key": key,
            "value": event.value
        })

        publish.single('devices/ble-remote/buttons/' + key, payload, hostname='192.168.1.112')
