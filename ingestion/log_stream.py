import random
from datetime import datetime, timedelta
USERS = [f"user_{i}" for i in range(1, 21)]
BASE_IPS = [
    "192.168.1.1",
    "10.0.0.5",
    "172.16.0.3",
    "192.168.0.8"
]
ACTIONS = ["login", "logout", "file_access", "admin_access"]
user_profiles = {
    user: {
        "home_ip": random.choice(BASE_IPS),
        "last_time": datetime.utcnow()
    }
    for user in USERS
}
def generate_log():
    user = random.choice(USERS)
    profile = user_profiles[user]
    delta = timedelta(seconds=random.randint(5, 30))
    profile["last_time"] += delta
    timestamp = profile["last_time"].isoformat()
    action = random.choices(
        ["login", "logout", "file_access"],
        weights=[0.4, 0.2, 0.4]
    )[0]
    ip = profile["home_ip"]
    if random.random() < 0.05:
        ip = f"203.0.113.{random.randint(1,255)}"
    if random.random() < 0.05:
        action = "admin_access"
    log = {
        "log_id": f"log_{random.randint(10000,99999)}",
        "user": user,
        "ip": ip,
        "action": action,
        "timestamp": timestamp
    }
    return log