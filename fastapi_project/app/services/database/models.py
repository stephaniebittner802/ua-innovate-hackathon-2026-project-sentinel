from typing import Optional
from datetime import datetime

from sqlmodel import Field, SQLModel
from .session import engine

# def configure():
#     SQLModel.metadata.create_all(bind=engine)

class Log(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    log: str
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)

class LiveIntelligenceReports(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    location: str
    resource_type: str
    stock_level: float

class HistoricStockLevels(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    location: str
    resource_type: str
    stock_level: float
    usage_rate_hourly: float
    snap_event: bool



# --- One-time DB setup (called from lifespan) ---
def configure(engine):
    """
    Create all tables for models registered on SQLModel.metadata.
    Call this from app startup (lifespan) to avoid side effects on import.
    """
    SQLModel.metadata.create_all(engine)
