import time
import json
import random

heart_rate = 70  # Initial heart rate

while True:
    time.sleep(1)  # Simulate heart rate reading every second
    heart_rate += random.randint(-1, 1)  # Random fluctuation
    with open('/tmp/heart_rate.json', 'w') as f:
        json.dump({'heart_rate': heart_rate}, f)
