from pydantic import BaseModel
from typing import Dict, Any
class LogEvent(BaseModel):
    log_id: str
    user: str
    ip: str
    action: str
    timestamp: str
class RiskResult(BaseModel):
    score: float
    level: str
    reasons: list
class PipelineResult(BaseModel):
    log: Dict[str, Any]
    ml_score: float
    rules: Dict[str, bool]
    risk: Dict[str, Any]
    explanation: Dict[str, Any] | str