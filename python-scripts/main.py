import json
import time

def read_step_count():
    with open('/tmp/step_count.json', 'r') as f:
        return json.load(f).get('steps', 0)

def read_location_data():
    with open('/tmp/location_data.json', 'r') as f:
        data = json.load(f)
        return data.get('distance', 0), data.get('location', (0, 0))

def read_heart_rate():
    with open('/tmp/heart_rate.json', 'r') as f:
        return json.load(f).get('heart_rate', 0)

def read_wifi_status():
    with open('/tmp/wifi_status.json', 'r') as f:
        return json.load(f).get('wifi_connected', False)

while True:
    steps = read_step_count()
    distance, location = read_location_data()
    heart_rate = read_heart_rate()
    wifi_connected = read_wifi_status()

    print(f'Steps: {steps}, Distance: {distance}, Location: {location}, Heart Rate: {heart_rate}, Wi-Fi Connected: {wifi_connected}')
    time.sleep(1)
