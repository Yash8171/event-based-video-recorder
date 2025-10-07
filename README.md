Hello\! I'd be happy to format your project documentation into a downloadable-ready `README.md` file structure.

Since I cannot directly create a downloadable file, I will provide the complete, properly structured Markdown content. You can copy and paste this into a file named `README.md`.

-----

```markdown
# 🎥 Event-Based Video Recorder (AI-Driven Prototype)

A **Python-based prototype system** for **event-driven video recording**, designed for applications like smart fleet monitoring or driver behavior detection.

It continuously buffers live video and saves event-triggered clips (e.g., Drowsiness, Mobile Usage, etc.) along with simulated metadata such as event type, timestamp, and GPS coordinates.

---

## 🚀 Features

✅ **Real-time camera capture** using OpenCV

✅ **Event-triggered recording** (manual or simulated AI events)

✅ **Buffered clips** (records **15s before** + **15s after** each event)

✅ **Metadata storage** in JSON + SQLite (event type, GPS, timestamp)

✅ **FastAPI backend** to list and download event clips

✅ **Mock event simulator** to emulate YOLO-based AI detection

✅ (Optional) Simple **HTML interface** to view saved clips

---

## 🧩 Project Structure

```

event\_recorder\_project/
├── clip\_writer.py        \# Handles saving buffered clips with metadata
├── event\_simulator.py    \# Simulates AI event detection (mock YOLO)
├── run\_capture.py        \# Main camera recording and event trigger logic
├── fastapi\_server.py     \# FastAPI backend to view/download clips
├── metadata\_db.py        \# Handles metadata storage in SQLite
├── events.db             \# SQLite database for events
├── metadata.json         \# JSON log for quick event info
├── requirements.txt      \# Python dependencies
├── README.md             \# Project documentation
├── .gitignore            \# Ignores venv, cache, etc.
└── /clips/               \# Stores saved event video clips

````

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone [https://github.com/Yash8171/event-based-video-recorder.git](https://github.com/Yash8171/event-based-video-recorder.git)
cd event-based-video-recorder
````

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate 
# OR On Linux/Mac
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

-----

## 🎬 Usage

### ▶️ Start live capture

```bash
python run_capture.py --source 0
```

Type `event` in the terminal to trigger an event manually.
Each event saves a 30-second clip (15s before + 15s after).
All clips are stored in the `/clips` folder with metadata.

### ⚡ Simulate AI event detection

```bash
python event_simulator.py --avg 30
```

This script randomly triggers simulated events like `Drowsiness`, `NoSeatBelt`, `MobileUsage`, etc., with an average interval of 30 seconds.

### 🌐 Run the FastAPI server

```bash
uvicorn fastapi_server:app --reload --port 8000
```

Then open:

  * `http://127.0.0.1:8000/events` → JSON list of saved events
  * `http://127.0.0.1:8000/events/html` → Simple web UI for clips
  * `http://127.0.0.1:8000/download/{filename}` → Download any clip

-----

## 🧠 Simulated Metadata

Each event clip saves details like the following example:

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

-----

## 🎥 Demo Video

[](https://www.google.com/search?q=https://youtu.be/YourVideoID)
**(Replace `YourVideoID` and the link with your actual YouTube or Google Drive video link)**

The video shows:

  * Live camera feed
  * Manual & simulated event triggers
  * Clip saving
  * FastAPI web interface usage

-----

## 🧑‍💻 Developer

**Yash Kumar Sahu**

  * B.Tech (CSE), SRMS College of Engineering & Technology
  * 📍 Gurgaon, India
  * [🌐 Portfolio](https://www.google.com/search?q=Your-Portfolio-Link)
  * [💼 LinkedIn](https://www.google.com/search?q=Your-LinkedIn-Link)
  * [💻 GitHub](https://www.google.com/search?q=Your-GitHub-Link)

-----

## 📄 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```
```