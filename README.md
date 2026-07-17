# 🏥 HealthGuard – Healthcare Data-Protection Study (Encryption, Audit, 2FA)

![CI](https://github.com/paulobiao/HealthGuard/actions/workflows/ci.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Encryption](https://img.shields.io/badge/Feature-Encryption%20%26%202FA-blue)](#)

> **Note:** This is an educational open-source project — a technical study of
> healthcare data-protection concepts (encryption, access auditing, 2FA
> simulation) using FastAPI and Docker. It is not a commercial product, has not
> been deployed in any production environment, and does not process real
> patient data. All sample data is synthetic.

**Objective**
Explore data encryption, access auditing, and risk-detection concepts for
healthcare-style systems, inspired by HIPAA privacy principles (educational
simulation only — this project makes no compliance claims).

---

## 🚀 Features
- Encryption-at-rest (AES-256) + integrity checks
- Access **audit logs** (who/when/what) with reason codes
- **2FA** (TOTP) simulation + RBAC (roles)
- FastAPI service + Docker + CI
- Synthetic sample data and demo scripts

---

## 🧠 Tech Stack
Python 3.11 • FastAPI • cryptography • PyJWT • SQLite/PostgreSQL • Docker • GitHub Actions

---

## ▶️ Quickstart
```bash
git clone https://github.com/paulobiao/HealthGuard.git
cd HealthGuard
pip install -r requirements.txt
uvicorn src.main:app --reload
docker build -t healthguard:0.1.0 .
docker run -p 8000:8000 healthguard:0.1.0
```

## 📁 Project Layout
```
src/
  healthguard/
    main.py        # FastAPI app & endpoints
    encryption.py  # AES encryption utilities
    audit.py       # access logging
    models.py      # schemas (synthetic patient-style data)
  tests/
    test_encryption.py
    test_audit.py
data/
  sample_medical_records.csv   # synthetic data
docs/
  hipaa_concepts.md
.github/workflows/ci.yml
Dockerfile
docker-compose.yml
requirements.txt
LICENSE
README.md
```
