from datetime import datetime, timedelta
def check_login_spike(log: dict, state: dict) -> bool:
    if log["action"] != "login":
        return False
    user = log["user"]
    time = datetime.fromisoformat(log["timestamp"])
    state.setdefault(user, {})
    state[user].setdefault("login_times", [])
    times = state[user]["login_times"]
    window = time - timedelta(minutes=2)
    times = [t for t in times if t > window]
    times.append(time)
    state[user]["login_times"] = times
    return len(times) >= 6