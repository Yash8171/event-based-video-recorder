from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from metadata_db import list_clips_simple, init_db
import os

app = FastAPI(title="Event Recorder API (v3)")

@app.on_event("startup")
def startup():
    init_db()
    from metadata_db import seed_fake_events
    seed_fake_events()

@app.get("/")
def root():
    return {"message": "Event Recorder API Running"}

@app.get("/events")
def get_events():
    return list_clips_simple()

@app.get("/events/html")
def list_events_html():
    data = list_clips_simple()  
    html = """
            <h2>🎥 Recorded Events</h2>
            <table border='1' cellpadding='8' style='border-collapse: collapse'>
            <tr><th>Timestamp</th><th>Event Type</th><th>Download</th></tr>
            """
    for e in data:
        html += f"<tr><td>{e['timestamp']}</td><td>{e['event_type']}</td><td><a href='/download/{e['filename']}'>Download</a></td></tr>"
    html += "</table>"
    return HTMLResponse(content=html) 

@app.get("/download/{filename}")
def download(filename: str):
    file_path = os.path.join("clips", filename)
    if not os.path.exists(file_path):
        return JSONResponse(status_code=404, content={"detail": "Not Found"})
    return FileResponse(file_path, media_type="video/mp4", filename=filename)
