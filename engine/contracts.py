from typing import Literal, Optional
from pydantic import BaseModel

RiskLevel = Literal["low", "medium", "high", "unknown"]

class RiskSignal(BaseModel):
    source: str = "ai-foundary"
    risk_level: RiskLevel
    evidence_id: Optional[str] = None
