from typing import Dict
import math
RULE_WEIGHTS = {
    "login_spike": 0.4,
    "ip_anomaly": 0.3,
    "privilege": 0.3
}
THRESHOLDS = {
    "low": 0,
    "medium": 30,
    "high": 60,
    "critical": 80
}
def _normalize_ml(score: float) -> float:
    return 1 / (1 + math.exp(5 * score))
def _ml_score(score: float) -> float:
    return _normalize_ml(score) * 100
def _rule_score(rules: Dict[str, bool]) -> float:
    score = 0
    active_rules = 0
    for rule, weight in RULE_WEIGHTS.items():
        if rules.get(rule, False):
            score += weight * 100
            active_rules += 1
    if active_rules == 1:
        score *= 0.7
    return score
def _generate_reasons(ml_score, rules) -> list:
    reasons = []
    if ml_score > 60:
        reasons.append("ML model detected anomalous behavior pattern")
    if rules.get("login_spike"):
        reasons.append("Multiple rapid login attempts detected")
    if rules.get("ip_anomaly"):
        reasons.append("Access from unfamiliar or new IP address")
    if rules.get("privilege"):
        reasons.append("Suspicious admin-level access behavior")
    return reasons
def compute_risk(ml_score_raw: float, rules: Dict[str, bool]) -> Dict:
    ml_score = _ml_score(ml_score_raw)
    rule_score = _rule_score(rules)
    if rule_score > 50:
        weight_ml = 0.4
        weight_rules = 0.6
    else:
        weight_ml = 0.6
        weight_rules = 0.4
    final_score = (
        weight_ml * ml_score +
        weight_rules * rule_score
    )
    if ml_score > 60 and sum(rules.values()) >= 2:
        final_score += 10
    final_score = min(100, round(final_score, 2))
    if final_score >= THRESHOLDS["critical"]:
        level = "critical"
    elif final_score >= THRESHOLDS["high"]:
        level = "high"
    elif final_score >= THRESHOLDS["medium"]:
        level = "medium"
    else:
        level = "low"
    reasons = _generate_reasons(ml_score, rules)
    return {
        "score": final_score,
        "level": level,
        "ml_score": round(ml_score, 2),
        "rule_score": round(rule_score, 2),
        "confidence": round((ml_score + rule_score) / 2, 2),
        "reasons": reasons
    }