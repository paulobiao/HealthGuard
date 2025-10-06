# Contributing to HealthGuard™

## Fluxo
1. Fork → branch `feat/...` → PR com descrição
2. Commits claros (`feat:`, `fix:`, `docs:` etc.)
3. Testes com `pytest` obrigatórios para módulos críticos

## Padrão de código
- Python 3.11+
- PEP8 + docstrings
- Não anexar qualquer PII real (use dados simulados)

## Rodando local
```bash
pip install -r requirements.txt
uvicorn src.healthguard.main:app --reload --port 8000
# docs: http://localhost:8000/docs
