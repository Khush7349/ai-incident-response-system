from typing import Dict, Any
def format_incident(result: Dict[str, Any]) -> Dict[str, Any]:
    log = result.get("log", {})
    risk = result.get("risk", {})
    rules = result.get("rules", {})
    explanation = result.get("explanation", {})
    return {
        "incident_id": log.get("log_id"),
        "user": log.get("user"),
        "ip": log.get("ip"),
        "action": log.get("action"),
        "risk_score": risk.get("score"),
        "risk_level": risk.get("level"),
        "flags": [k for k, v in rules.items() if v],
        "summary": explanation.get("summary"),
        "confidence": explanation.get("confidence")
    }