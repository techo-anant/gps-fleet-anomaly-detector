import random
import pandas as pd
from datetime import datetime, timedelta

def generate_data( vehicle_id, num_points=100):
    data = []
    timestamp = datetime.now()
    lat , lon = 43.6532, -79.3832 

    for _ in range(num_points):
        # randomly generate the current speed of vehicle
        speed = random.uniform(0, 120)

        # Assuming 5% prob of harsh breaking if speed is more tham 80kmph
        harsh_brake = speed > 80 and random.random() > 0.95

        data.append({
            'vehicle_id': vehicle_id,
            'timestamp': timestamp,
            'latitude': lat,
            'longitude': lon,
            'speed_kmph': speed,
            'harsh_brake_event': harsh_break
        })

        timestamp += timedelta(seconds=30)
        lat += random.uniform(-0.001, 0.001)
        lon += random.uniform(-0.001, 0.001)
    
    return pd.DataFrame(data)


df = pd.concat([generate_data(f'ID-{i:03d}') for i in range(5)])
df.to_csv('fleet_data.csv', index=False)


