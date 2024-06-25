import time
import json
import random

step_count = 0

while True:
    time.sleep(1)  
    step_count += random.randint(1, 5) 
    with open('/tmp/step_count.json', 'w') as f:
        json.dump({'steps': step_count}, f)
