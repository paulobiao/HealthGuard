
# HealthGuard™ – Healthcare Data Protection Framework

Protects simulated EHR data with encryption-at-rest, 2FA auth, access logging, and basic compliance reporting (HIPAA/LGPD). Built for portfolio-grade demonstration and EB2-NIW evidence.

## Features
- FastAPI with JWT + TOTP (2FA)
- AES-GCM encryption for patient records (at-rest)
- Access log & simple compliance report (`/api/v1/compliance/report`)
- Batch import/export CSV for demo
- Docker & CI ready

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn healthguard.main:app --reload --port 8000
# http://localhost:8000/docs
```
