def check_ip_anomaly(log: dict, state: dict) -> bool:
    user = log["user"]
    ip = log["ip"]
    state.setdefault(user, {})
    state[user].setdefault("known_ips", set())
    known_ips = state[user]["known_ips"]
    if len(known_ips) < 3:
        known_ips.add(ip)
        return False
    is_new = ip not in known_ips
    known_ips.add(ip)
    return is_new