def check_privilege_misuse(log: dict, state: dict) -> bool:
    user = log["user"]
    action = log["action"]
    state.setdefault(user, {})
    state[user].setdefault("admin_count", 0)
    if action == "admin_access":
        state[user]["admin_count"] += 1
        return state[user]["admin_count"] > 3
    return False