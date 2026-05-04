import time
from ingestion.preprocessing import preprocess_log
from detectors.isolation import detect_isolation
from rules.login_spike import check_login_spike
from rules.ip_anomaly import check_ip_anomaly
from rules.privilege import check_privilege_misuse
from scoring.risk_engine import compute_risk
from intelligence.llm_agent import explain_incident
from intelligence.formatter import format_incident
def run_pipeline(log: dict, state: dict):
    start = time.time()
    try:
        log = preprocess_log(log)
        ml_score = detect_isolation(log)
        rules = {
            "login_spike": check_login_spike(log, state),
            "ip_anomaly": check_ip_anomaly(log, state),
            "privilege": check_privilege_misuse(log, state)
        }
        risk = compute_risk(ml_score, rules)
        explanation = explain_incident(log, rules, risk)
        result = {
            "log": log,
            "ml_score": ml_score,
            "rules": rules,
            "risk": risk,
            "explanation": explanation
        }
        formatted = format_incident(result)
        formatted["latency_ms"] = round((time.time() - start) * 1000, 2)
        return formatted
    except Exception as e:
        return {
            "error": str(e),
            "log": log
        }