import pytest
from httpx import ASGITransport, AsyncClient
from src.api.main import app

@pytest.fixture
async def client():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c

@pytest.mark.asyncio
async def test_health(client):
    assert (await client.get("/api/v1/health")).status_code == 200

@pytest.mark.asyncio
async def test_churn_prediction(client):
    payload = {"customer_id": "C-001", "tenure_months": 6, "monthly_charges": 89.99,
               "total_charges": 540, "contract_type": "month-to-month",
               "payment_method": "electronic_check", "internet_service": "Fiber_optic",
               "gender": "Female", "senior_citizen": 0, "partner": "No",
               "dependents": "No", "online_security": "No_internet",
               "tech_support": "No_internet", "paperless_billing": "Yes", "num_tickets": 5}
    r = await client.post("/api/v1/analyze/churn", json=payload)
    assert r.status_code == 200
    d = r.json()
    assert 0 <= d["churn_probability"] <= 1
    assert d["risk_tier"] in ("low", "medium", "high", "critical")

@pytest.mark.asyncio
async def test_segments(client):
    r = await client.get("/api/v1/analyze/segments")
    assert r.status_code == 200
    assert len(r.json()) > 0

@pytest.mark.asyncio
async def test_rfm(client):
    r = await client.post("/api/v1/analyze/rfm?customer_id=C-999")
    assert r.status_code == 200
    d = r.json()
    assert "rfm_score" in d
    assert "segment" in d
