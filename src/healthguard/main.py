
from fastapi import FastAPI, HTTPException
from .models import RecordIn, Token
from .utils import encrypt, decrypt
from pydantic import BaseModel
import json

app = FastAPI(title="HealthGuard API", version="0.1.0")

DB = {}
AUDIT = []

class Score(BaseModel):
    ok: bool

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/api/v1/record/encrypt")
def add_record(rec: RecordIn):
    enc = encrypt(json.dumps(rec.model_dump()).encode())
    DB[rec.patient.patient_id] = enc
    AUDIT.append({"event":"WRITE","pid": rec.patient.patient_id})
    return {"stored": True}

@app.get("/api/v1/record/{pid}")
def get_record(pid: str):
    if pid not in DB: raise HTTPException(404, "not found")
    AUDIT.append({"event":"READ","pid": pid})
    data = json.loads(decrypt(DB[pid]).decode())
    return data

@app.get("/api/v1/compliance/report")
def compliance():
    return {
        "encrypted_records": len(DB),
        "audit_events": len(AUDIT),
        "2fa": "TOTP (stub)",
        "hipaa_controls": ["encryption-at-rest", "access-logs"]
    }
