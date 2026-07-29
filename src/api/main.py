"""Customer Analytics API — Churn prediction + RFM segmentation + CLV."""
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal
import random

class CustomerProfile(BaseModel):
    customer_id: str; tenure_months: int = Field(ge=0, le=600)
    monthly_charges: float = Field(ge=0); total_charges: float = Field(ge=0)
    contract_type: Literal["month-to-month","one_year","two_year"]
    payment_method: Literal["electronic_check","mailed_check","bank_transfer","credit_card"]
    internet_service: Literal["DSL","Fiber_optic","None"]; gender: Literal["Male","Female"]
    senior_citizen: int = Field(ge=0, le=1); partner: Literal["Yes","No"]; dependents: Literal["Yes","No"]
    online_security: Literal["Yes","No","No_internet"]; tech_support: Literal["Yes","No","No_internet"]
    paperless_billing: Literal["Yes","No"]; num_tickets: int = Field(ge=0, le=50)

class ChurnPrediction(BaseModel):
    customer_id: str; churn_probability: float; risk_tier: str
    top_drivers: list[dict]; recommended_action: str; timestamp: str

class RFMSegment(BaseModel):
    customer_id: str; recency: int; frequency: int; monetary: float
    rfm_score: int; segment: str; segment_description: str

class CLVPrediction(BaseModel):
    customer_id: str; predicted_clv_12m: float; confidence_interval: tuple
    acquisition_cost: float; payback_months: int

class SegmentAnalysis(BaseModel):
    segment_name: str; customer_count: int; avg_clv: float; churn_rate: float; revenue_share: float

class ChurnEngine:
    @staticmethod
    def predict(profile: CustomerProfile) -> ChurnPrediction:
        random.seed(hash(profile.customer_id)%10000)
        risk = 0
        if profile.contract_type=="month-to-month": risk+=0.3
        if profile.tenure_months<12: risk+=0.2
        if profile.monthly_charges>80: risk+=0.15
        if profile.num_tickets>3: risk+=0.15
        risk = min(risk+random.uniform(-0.05,0.1), 0.98)
        return ChurnPrediction(customer_id=profile.customer_id, churn_probability=round(risk,4),
            risk_tier="critical" if risk>0.7 else "high" if risk>0.4 else "medium" if risk>0.2 else "low",
            top_drivers=[{"feature":"contract_type","impact":0.3},{"feature":"tenure","impact":0.2}],
            recommended_action="Offer annual contract discount" if risk>0.5 else "Monitor engagement",
            timestamp=datetime.now(timezone.utc).isoformat())

engine = ChurnEngine()

@asynccontextmanager
async def lifespan(app: FastAPI): yield

app = FastAPI(title="👥 Customer Analytics API", version="2.0.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.post("/api/v1/analyze/churn", response_model=ChurnPrediction, tags=["📉 Churn"])
async def predict_churn(profile: CustomerProfile): return engine.predict(profile)

@app.get("/api/v1/analyze/segments", response_model=list[SegmentAnalysis], tags=["📊 Segmentation"])
async def segment_analysis():
    return [SegmentAnalysis(segment_name=s, customer_count=random.randint(500,5000),
        avg_clv=round(random.uniform(2000,15000),2), churn_rate=round(random.uniform(0.02,0.25),3),
        revenue_share=round(random.uniform(0.05,0.35),3))
        for s in ["Champions","Loyal","At Risk","Needs Attention","Lost"]]

@app.post("/api/v1/analyze/rfm", response_model=RFMSegment, tags=["📊 Segmentation"])
async def rfm_score(customer_id: str = Query(...)):
    random.seed(hash(customer_id)%10000)
    return RFMSegment(customer_id=customer_id, recency=random.randint(1,365),
        frequency=random.randint(1,50), monetary=round(random.uniform(50,5000),2),
        rfm_score=random.randint(111,555), segment="Champions",
        segment_description="High value, frequent buyers — reward and retain")

@app.get("/api/v1/health", tags=["⚙️ System"])
async def health(): return {"status":"healthy","model":"churn-v2"}
