import pandas as pd
ACTION_MAP = {
    "login": 0,
    "logout": 1,
    "file_access": 2,
    "admin_access": 3
}
def extract_features(log: dict):
    df = pd.DataFrame([log])
    df["action_code"] = df["action"].map(ACTION_MAP).fillna(-1)
    df["is_admin_action"] = (df["action"] == "admin_access").astype(int)
    return df[["action_code", "is_admin_action"]].values