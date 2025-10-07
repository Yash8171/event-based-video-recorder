# 🎯 Event-Based Video Recording Using AI Event Detection

## 🚀 Overview
This project simulates an AI-powered event detection system (like YOLO) that triggers 30-second video recordings — capturing 15s before and 15s after each event.

## 🧩 Components
- **run_capture.py** → Captures video, buffers frames, saves clips when an event occurs.
- **event_simulator.py** → Randomly triggers mock events.
- **fastapi_server.py** → Lists and downloads saved clips via REST API.

## ⚙️ Setup Instructions
1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the capture system:
   ```bash
   python run_capture.py --source 0
   ```
4. In another terminal, start event simulator:
   ```bash
   python event_simulator.py
   ```
5. To view/download recorded clips:
   ```bash
   uvicorn fastapi_server:app --reload --port 8000
   ```
   - View events: http://127.0.0.1:8000/events
   - Download: http://127.0.0.1:8000/download/<filename>

## 📁 Output
- Saved clips → `recordings/`
- Metadata → `metadata.json`

## 💡 Features
- Simulated GPS coordinates
- Manual or automatic event triggering
- 30-second recording window per event
- Simple FastAPI backend to browse clips
