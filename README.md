# 👥 ML Customer Analytics

[![CI/CD](https://github.com/twomathematicians-code/ml-customer-analytics/actions/workflows/ci.yml/badge.svg)](https://github.com/twomathematicians-code/ml-customer-analytics/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](https://hub.docker.com/)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)

**End-to-end customer analytics pipeline: churn prediction, RFM segmentation, customer lifetime value, and explainable AI with SHAP — built for marketing & retention teams.**

---

## 🎯 Analytics Modules

| Module | Algorithm | Output |
|---|---|---|
| **Churn Prediction** | XGBoost + SHAP | Risk score + feature drivers |
| **Customer Segmentation** | K-Means + RFM Analysis | 5-tier segmentation |
| **Lifetime Value (CLV)** | BG/NBD + Gamma-Gamma | 12-month CLV projection |
| **Cohort Analysis** | Retention curves | Monthly cohort heatmaps |

---

## 🚀 Quick Start

```bash
git clone https://github.com/twomathematicians-code/ml-customer-analytics.git
cd ml-customer-analytics
docker-compose up --build
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/v1/analyze/churn` | Churn risk prediction |
| `POST` | `/api/v1/analyze/segment` | Customer segmentation |
| `POST` | `/api/v1/analyze/clv` | Lifetime value prediction |
| `GET` | `/api/v1/health` | Health check |

---

## 👤 Author

**Mahesh Solanki** — [LinkedIn](https://linkedin.com/in/maheshsolanki-16b9a6a5) | [GitHub](https://github.com/twomathematicians-code)
