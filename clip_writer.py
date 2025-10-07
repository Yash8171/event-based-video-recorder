import cv2
import os
from datetime import datetime
from metadata_db import insert_clip
import random

CLIPS_DIR = os.path.join(os.path.dirname(__file__), "clips")
os.makedirs(CLIPS_DIR, exist_ok=True)

def _simulate_gps():
    base_lat, base_lon = 28.5355, 77.3910
    jitter = lambda: (random.random() - 0.5) * 0.02
    return base_lat + jitter(), base_lon + jitter()

def write_clip(frames, fps, event_type, post_frames=None):
    if post_frames:
        frames = frames + post_frames
    if len(frames) == 0:
        return None
    timestamp_str = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = f"clip_{event_type}_{timestamp_str}.mp4"
    fullpath = os.path.join(CLIPS_DIR, filename)
    _, first = frames[0]
    h, w = first.shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(fullpath, fourcc, fps, (w, h))
    for ts, frame in frames:
        writer.write(frame)
    writer.release()
    event_ts = frames[0][0] if frames else datetime.utcnow().isoformat()
    duration = len(frames) / float(fps) if fps else None
    lat, lon = _simulate_gps()
    insert_clip(filename, event_type, event_ts, lat, lon, duration)
    print(f"[clip_writer] Saved {fullpath} ({duration:.2f}s) GPS=({lat:.5f},{lon:.5f})")
    return fullpath
