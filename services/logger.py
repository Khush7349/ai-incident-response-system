from datetime import datetime
def log_event(event_type: str, data: dict):
    print({
        "time": datetime.utcnow().isoformat(),
        "type": event_type,
        "data": data
    })