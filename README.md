# 👥 Customer Analytics Platform

[![CI](https://github.com/twomathematicians-code/customer-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/twomathematicians-code/customer-analytics/actions)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.0-06b6d4?logo=xgboost)](https://xgboost.readthedocs.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://hub.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Churn Prediction · RFM Segmentation · CLV Estimation · SHAP Explainability

```
pip install -e ".[dev]"
docker compose up -d
pytest tests/
```

---

## What It Does

| Capabilities | Model | Output |
|:--|:--|:--|
| Churn Risk Scoring | XGBoost + SHAP | Probability + reason codes |
| RFM Segmentation | Quantile-based RFM | Tier labels (Champions, At Risk...) |
| Customer Lifetime Value | BG/NBD + Gamma-Gamma | 12-month monetary projection |
| Cohort Analysis | Retention curves | Monthly heatmaps |

## Running

```bash
# Full stack
docker compose up --build

# Predict churn for a customer
curl -X POST http://localhost:8000/api/v1/analyze/churn -H "Content-Type: application/json" -d '{
  "customer_id": "C-12345",
  "tenure_months": 8,
  "monthly_charges": 85.50,
  "total_charges": 684.00,
  "contract_type": "month-to-month",
  "payment_method": "electronic_check",
  "internet_service": "Fiber_optic",
  "gender": "Male",
  "senior_citizen": 0,
  "partner": "No",
  "dependents": "No",
  "online_security": "No_internet",
  "tech_support": "No_internet",
  "paperless_billing": "Yes",
  "num_tickets": 4
}'
```

## Endpoints

- `POST /api/v1/analyze/churn` — Single customer churn prediction
- `GET  /api/v1/analyze/segments` — Segment-level analytics
- `POST /api/v1/analyze/rfm` — RFM scoring for a customer
- `GET  /api/v1/health` — Health check

## Project Structure

```
├── src/
│   ├── api/main.py          # FastAPI endpoints
│   ├── models/train.py      # XGBoost churn model + SHAP
│   ├── utils/config.py      # App settings
│   └── utils/logging.py     # Structured logging
├── tests/test_api.py        # Integration tests
├── configs/model_config.yaml
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

## Stack

Python 3.11 · FastAPI · XGBoost · LightGBM · SHAP · pandas · PostgreSQL · Docker

---

<p align="center">
  <a href="https://linkedin.com/in/maheshsolanki-16b9a6a5">Mahesh Solanki</a> ·
  <a href="https://github.com/twomathematicians-code">GitHub</a>
</p>
# Update
