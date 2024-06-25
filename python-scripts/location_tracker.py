import time
import json
import random

locations = [(0, 0), (1, 1), (2, 2), (3, 3)]  
distance_walked = 0
current_location = (0, 0)

while True:
    time.sleep(5)  
    new_location = random.choice(locations)
    distance = ((new_location[0] - current_location[0])**2 + (new_location[1] - current_location[1])**2) ** 0.5
    distance_walked += distance
    current_location = new_location
    with open('/tmp/location_data.json', 'w') as f:
        json.dump({'distance': distance_walked, 'location': current_location}, f)
