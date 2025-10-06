from fastapi.testclient import TestClient
from src.healthguard.main import app

def test_encrypt_and_audit():
    c = TestClient(app)
    r = c.post("/api/v1/encrypt", json={"patient_id":"p1","data":"ok"})
    assert r.status_code == 200
    a = c.get("/api/v1/audit")
    assert a.status_code == 200
    assert len(a.json().get("entries", [])) >= 1
