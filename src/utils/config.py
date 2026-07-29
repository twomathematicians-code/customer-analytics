from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://cust:cust123@localhost:5432/customer_db"
    churn_threshold: float = 0.4
    rfm_quantiles: list = [0.25, 0.5, 0.75]

@lru_cache
def get_settings() -> Settings:
    return Settings()
