from fastapi import FastAPI, Request
from datetime import datetime
import json
import os

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ok": True, "now": datetime.utcnow().isoformat() + "Z"}

@app.post("/save")
async def save_log(request: Request):
    body = await request.json()
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"raven_log_{timestamp}.json"

    # Save to local file (Render ephemeral storage)
    with open(filename, "w") as f:
        json.dump(body, f, indent=2)

    return {"ok": True, "saved_as": filename}
