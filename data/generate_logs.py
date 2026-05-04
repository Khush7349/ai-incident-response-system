import pandas as pd
import random
from datetime import datetime, timedelta
N = 1000  
USERS = [f"user_{i}" for i in range(1, 21)]
IPS = ["192.168.1.1", "10.0.0.5", "172.16.0.3", "192.168.0.8"]
ACTIONS = ["login", "logout", "file_access", "admin_access"]
data = []
start_time = datetime(2024, 1, 1, 10, 0, 0)
for i in range(N):
    timestamp = start_time + timedelta(seconds=i * random.randint(5, 30))
    user = random.choice(USERS)
    ip = random.choice(IPS)
    action = random.choice(ACTIONS)
    if random.random() < 0.05:
        action = "admin_access"  
    if random.random() < 0.05:
        ip = f"203.0.113.{random.randint(1,255)}"  
    data.append({
        "log_id": f"log_{i}",
        "user": user,
        "ip": ip,
        "action": action,
        "timestamp": timestamp.isoformat()
    })
df = pd.DataFrame(data)
df.to_csv("data/logs.csv", index=False)
print(f"✅ Generated {N} logs")