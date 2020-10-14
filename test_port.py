import os
import time
import sys
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = '192.168.108.62'
ACCESS_TOKEN = 'pass0001'
#ACCESS_TOKEN = '2CZLCX4c6PcbmtFuez7x'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2

sensor_data = {'temperature': 0, 'humidity': 0}

next_reading = time.time() 

client = mqtt.Client()

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)
#client.connect(THINGSBOARD_HOST, 1883, 60)


client.loop_start()

try:
    while True:
        sensor_data['temperature'] = 35.1
        sensor_data['humidity'] = 66

        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()