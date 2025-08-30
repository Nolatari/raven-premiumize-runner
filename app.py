from fastapi import FastAPI, Request
import datetime
import json

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Raven runner live"}

@app.post("/save")
async def save_log(request: Request):
    body = await request.json()
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = f"RavenSnapshot_{timestamp}.json"

    # Save snapshot to local (GitHub Actions will commit it)
    with open(filename, "w") as f:
        json.dump(body, f, indent=2)

    return {"ok": True, "file": filename}
