from typing import Dict, Any
from datetime import datetime
def preprocess_log(log: Dict[str, Any]) -> Dict[str, Any]:
    log = log.copy()
    log["user"] = str(log.get("user", "")).lower().strip()
    log["ip"] = str(log.get("ip", "")).strip()
    log["action"] = str(log.get("action", "")).lower().strip()
    ts = log.get("timestamp")
    try:
        datetime.fromisoformat(ts)
    except:
        log["timestamp"] = datetime.utcnow().isoformat()
    return log