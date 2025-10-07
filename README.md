# 🎥 Event-Based Video Recorder (AI-Driven Prototype)

A Python-based prototype system for event-driven video recording, designed for applications like smart fleet monitoring or driver behavior detection.
It continuously buffers live video and saves event-triggered clips (e.g., Drowsiness, Mobile Usage, etc.) along with simulated metadata such as event type, timestamp, and GPS coordinates.

## 🚀 Features

✅ Real-time camera capture using OpenCV  
✅ Event-triggered recording (manual or simulated AI events)  
✅ Buffered clips (records 15s before + 15s after each event)  
✅ Metadata storage in JSON + SQLite (event type, GPS, timestamp)  
✅ FastAPI backend to list and download event clips  
✅ Mock event simulator to emulate YOLO-based AI detection  
✅ (Optional) Simple HTML interface to view saved clips  

## 🧩 Project Structure
```
event_recorder_project/
├── clip_writer.py        # Handles saving buffered clips with metadata
├── event_simulator.py    # Simulates AI event detection (mock YOLO)
├── run_capture.py        # Main camera recording and event trigger logic
├── fastapi_server.py     # FastAPI backend to view/download clips
├── metadata_db.py        # Handles metadata storage in SQLite
├── events.db             # SQLite database for events
├── metadata.json         # JSON log for quick event info
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Ignores venv, cache, etc.
└── /clips/               # Stores saved event video clips
```

## ⚙️ Installation

1️⃣ Clone the repository  
```bash
git clone https://github.com/Yash8171/event-based-video-recorder.git
cd event-based-video-recorder
```

2️⃣ Create & activate virtual environment  
```bash
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Linux/Mac
```

3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

## 🎬 Usage

▶️ Start live capture  
```bash
python run_capture.py --source 0
```

Type `event` in terminal to trigger an event manually.  
Each event saves a 30-second clip (15s before + 15s after).  
All clips are stored in the `/clips` folder with metadata.

## ⚡ Simulate AI event detection

```bash
python event_simulator.py --avg 30
```

This script randomly triggers simulated events like Drowsiness, NoSeatBelt, MobileUsage, etc.

## 🌐 Run the FastAPI server

```bash
uvicorn fastapi_server:app --reload --port 8000
```

Then open:

- [http://127.0.0.1:8000/events](http://127.0.0.1:8000/events) → JSON list of saved events  
- [http://127.0.0.1:8000/events/html](http://127.0.0.1:8000/events/html) → Simple web UI for clips  
- [http://127.0.0.1:8000/download/{filename}](http://127.0.0.1:8000/download/{filename}) → Download any clip

## 🧠 Simulated Metadata

Each event clip saves details like:

```json
{
  "id": 1,
  "filename": "clip_Drowsiness_20251007T104500Z.mp4",
  "event_type": "Drowsiness",
  "timestamp": "2025-10-07T10:45:00Z",
  "gps_lat": 28.5449,
  "gps_lon": 77.3847,
  "duration": 30.0
}
```

## 🎥 Demo Video

📹 **Watch Demonstration Video**  
(Add your YouTube or Google Drive video link here)

The video shows:
- Live camera feed
- Manual & simulated event triggers
- Clip saving
- FastAPI web interface usage

## 🧑‍💻 Developer

**Yash Kumar Sahu**  
B.Tech (CSE), SRMS College of Engineering & Technology  
📍 Gurgaon, India  
🌐 [Portfolio]()  
💼 [LinkedIn]()  
💻 [GitHub]()  

## 📄 License

This project is open-source and available under the **MIT License**.
