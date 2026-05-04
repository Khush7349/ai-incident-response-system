import requests
import json
import re
from typing import Dict, Any
from config import OLLAMA_URL, LLM_MODEL
def _extract_json(text: str) -> str:
    """
    Extract JSON object from model output safely
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    return match.group(0) if match else ""
def _safe_parse(text: str) -> Dict[str, Any]:
    try:
        j = _extract_json(text)
        return json.loads(j) if j else {}
    except:
        return {}
def _call_llm(prompt: str) -> str:
    for _ in range(2):  
        try:
            res = requests.post(
                OLLAMA_URL,
                json={
                    "model": LLM_MODEL,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.2
                    }
                },
                timeout=15
            )
            res.raise_for_status()
            return res.json().get("response", "").strip()
        except:
            continue
    return ""
def explain_incident(
    log: Dict[str, Any],
    rules: Dict[str, bool],
    risk: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Generate structured explanation for security incident
    """
    if risk.get("level") not in ["high", "critical"]:
        return {
            "summary": "Low risk activity",
            "reasons": [],
            "confidence": "low"
        }
    prompt = f"""
You are a cybersecurity analyst.
Return ONLY a valid JSON object. No text before or after.
FORMAT:
{{
  "summary": "...",
  "reasons": ["...", "..."],
  "confidence": "low/medium/high"
}}
--- LOG ---
User: {log.get("user")}
IP: {log.get("ip")}
Action: {log.get("action")}
Timestamp: {log.get("timestamp")}
--- RULE SIGNALS ---
Login Spike: {rules.get("login_spike")}
IP Anomaly: {rules.get("ip_anomaly")}
Privilege Misuse: {rules.get("privilege")}
--- RISK ---
Score: {risk.get("score")}
Level: {risk.get("level")}
Reasons: {risk.get("reasons")}
Rules:
- Use only given data
- Do not hallucinate
- Keep output concise
"""
    raw = _call_llm(prompt)
    parsed = _safe_parse(raw)
    if not parsed:
        return {
            "summary": "Suspicious activity detected based on anomaly signals",
            "reasons": risk.get("reasons", []),
            "confidence": "medium"
        }
    return {
        "summary": parsed.get("summary", ""),
        "reasons": parsed.get("reasons", []),
        "confidence": parsed.get("confidence", "medium")
    }