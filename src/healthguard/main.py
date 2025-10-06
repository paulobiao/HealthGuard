from fastapi import FastAPI
from pydantic import BaseModel
from cryptography.fernet import Fernet
import time, os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="HealthGuard API", version="0.2.0")

KEY = os.getenv("HEALTHGUARD_KEY")
if not KEY:
    # fallback inseguro para demo; use .env em produção
    KEY = Fernet.generate_key().decode()
cipher = Fernet(KEY.encode())
audit_log = []

class Record(BaseModel):
    patient_id: str
    data: str

@app.post("/api/v1/encrypt")
def encrypt_record(rec: Record):
    token = cipher.encrypt(rec.data.encode())
    audit_log.append({"patient_id": rec.patient_id, "action": "encrypt", "timestamp": time.time()})
    return {"encrypted": token.decode(), "audit_count": len(audit_log)}

@app.get("/api/v1/audit")
def get_audit():
    return {"entries": audit_log[-5:]}

@app.post("/api/v1/key/rotate")
def rotate_key():
    """Simula rotação de chave (gera nova Fernet key)."""
    global cipher, KEY
    KEY = Fernet.generate_key().decode()
    cipher = Fernet(KEY.encode())
    audit_log.append({"action": "rotate_key", "timestamp": time.time()})
    return {"ok": True, "new_key_set": True, "audit_count": len(audit_log)}
