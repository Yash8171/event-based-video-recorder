import time
import random
import json
from datetime import datetime

def simulate_event(avg_interval=45):
    print(f"[simulator] Running mock event generator (avg {avg_interval}s per event)...")
    while True:
        sleep_time = max(5, random.gauss(avg_interval, 10))
        time.sleep(sleep_time)

        event = {
            "event_type": random.choice(["Drowsiness", "MobileUsage", "NoSeatBelt", "Yawning"]),
            "timestamp": datetime.now().isoformat(),
        }
        with open("event_trigger.json", "w") as f:
            json.dump(event, f)

        print(f"[simulator] Triggered: {event['event_type']} at {event['timestamp']}")

if __name__ == "__main__":
    simulate_event(avg_interval=45)
