import cv2
import time
import json
import os
import threading
import random
from datetime import datetime, timedelta
from clip_writer import write_clip

# Global variables
BUFFER_DURATION = 15  # seconds
POST_EVENT_DURATION = 15  # seconds after event
FPS = 10
frame_buffer = []
last_event = None
event_end_time = None

# Folder setup
CLIPS_DIR = os.path.join(os.path.dirname(__file__), "clips")
os.makedirs(CLIPS_DIR, exist_ok=True)

def get_random_gps():
    return [round(random.uniform(28.60, 28.65), 5),
            round(random.uniform(77.20, 77.25), 5)]

def read_event():
    if os.path.exists("event_trigger.json"):
        try:
            with open("event_trigger.json", "r") as f:
                data = json.load(f)
            os.remove("event_trigger.json")
            return data
        except Exception:
            return None
    return None

def event_listener():
    global last_event, event_end_time
    while True:
        inp = input("Type 'event' to trigger, 'exit' to quit: ").strip().lower()
        if inp == "event":
            last_event = "ManualTrigger"
            event_end_time = datetime.now() + timedelta(seconds=POST_EVENT_DURATION)
            threading.Thread(target=write_clip, args=(frame_buffer.copy(), FPS, "ManualTrigger"), daemon=True).start()
            print(f"[event] Clip recorded for ManualTrigger")
        elif inp == "exit":
            print("[system] Exiting capture...")
            os._exit(0)

def capture_video(source=0):
    global last_event, event_end_time
    cap = cv2.VideoCapture(source, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("[error] Unable to open camera.")
        return

    print(f"[main] Camera initialized: {int(cap.get(3))}x{int(cap.get(4))} @ {FPS}fps")
    print("[main] Capture started. Type 'event' to trigger, 'q' to quit preview.")

    # Start manual event thread
    threading.Thread(target=event_listener, daemon=True).start()

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (640, 480))
        frame_buffer.append((datetime.now(), frame))
        if len(frame_buffer) > BUFFER_DURATION * FPS:
            frame_buffer.pop(0)

        # Check simulated AI events
        event_data = read_event()
        if event_data:
            last_event = event_data.get("event_type", "AI_Trigger")
            event_end_time = datetime.now() + timedelta(seconds=POST_EVENT_DURATION)
            threading.Thread(target=write_clip, args=(frame_buffer.copy(), FPS, last_event), daemon=True).start()
            print(f"[event] AI Clip recorded for {last_event}")

        # Overlay info on frame
        countdown_text = ""
        if event_end_time:
            remaining = (event_end_time - datetime.now()).total_seconds()
            if remaining > 0:
                countdown_text = f" | Post-event recording: {int(remaining)}s"
            else:
                countdown_text = ""
                event_end_time = None

        info_text = f"Buffered Frames: {len(frame_buffer)} | Last Event: {last_event or 'None'}{countdown_text}"
        cv2.putText(frame, info_text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)

        # Add red border if recording post-event
        if event_end_time and (event_end_time - datetime.now()).total_seconds() > 0:
            color = (0, 0, 255)  # Red
            thickness = 4
            cv2.rectangle(frame, (0, 0), (frame.shape[1], frame.shape[0]), color, thickness)

        # Display
        cv2.imshow("Live Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video(0)
