import sqlite3
import os
from datetime import datetime
import json
import random

DB_PATH = os.path.join(os.path.dirname(__file__), "events.db")
JSON_MIRROR = os.path.join(os.path.dirname(__file__), "clips", "metadata.json")

def init_db():
    os.makedirs(os.path.join(os.path.dirname(__file__), "clips"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS clips (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            event_type TEXT,
            timestamp TEXT,
            gps_lat REAL,
            gps_lon REAL,
            duration REAL
        )
    ''')
    conn.commit()
    conn.close()
    _mirror_json()

def insert_clip(filename, event_type, timestamp, gps_lat, gps_lon, duration):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO clips (filename, event_type, timestamp, gps_lat, gps_lon, duration)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (filename, event_type, timestamp, gps_lat, gps_lon, duration))
    conn.commit()
    conn.close()
    _mirror_json()

def list_clips():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, filename, event_type, timestamp, gps_lat, gps_lon, duration FROM clips ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

def _mirror_json():
    rows = list_clips_simple()
    with open(JSON_MIRROR, "w") as f:
        json.dump(rows, f, indent=2, default=str)

def list_clips_simple():
    if not os.path.exists(DB_PATH):
        return []
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT id, filename, event_type, timestamp, gps_lat, gps_lon, duration FROM clips ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return [
        {
            "id": r[0],
            "filename": r[1],
            "event_type": r[2],
            "timestamp": r[3],
            "gps_lat": r[4],
            "gps_lon": r[5],
            "duration": r[6]
        } for r in rows
    ]

def seed_fake_events():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Use clips table
    cursor.execute('''
        INSERT INTO clips (filename, event_type, timestamp, gps_lat, gps_lon, duration)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        "clip_Dummy.mp4",
        "ManualTrigger",
        datetime.now().isoformat(),
        28.54,
        77.38,
        30.0
    ))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("DB initialized.")
