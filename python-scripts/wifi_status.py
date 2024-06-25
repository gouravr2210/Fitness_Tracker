import time
import json
import subprocess

def get_wifi_status():
    result = subprocess.run(['nmcli', '-t', '-f', 'ACTIVE', 'connection', 'show', '--active'], stdout=subprocess.PIPE)
    return 'wifi' in result.stdout.decode('utf-8')

while True:
    time.sleep(10)  
    wifi_connected = get_wifi_status()
    with open('/tmp/wifi_status.json', 'w') as f:
        json.dump({'wifi_connected': wifi_connected}, f)
