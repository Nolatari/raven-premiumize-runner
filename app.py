from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ok": True, "now": datetime.utcnow().isoformat() + "Z"}

