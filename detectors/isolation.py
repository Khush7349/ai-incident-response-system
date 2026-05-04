import os
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from detectors.features import extract_features
from config import ISOLATION_MODEL_PATH
def train_isolation(df: pd.DataFrame):
    print("🔧 Training Isolation Forest...")
    X = _prepare_features(df)
    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )
    model.fit(X)
    os.makedirs(os.path.dirname(ISOLATION_MODEL_PATH), exist_ok=True)
    with open(ISOLATION_MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"✅ Model saved at {ISOLATION_MODEL_PATH}")
def detect_isolation(log: dict) -> float:
    model = _load_model()
    X = extract_features(log)
    score = model.decision_function(X)[0]
    return float(score)
def _load_model():
    if not os.path.exists(ISOLATION_MODEL_PATH):
        raise Exception("❌ Isolation model not trained. Run train.py")
    with open(ISOLATION_MODEL_PATH, "rb") as f:
        return pickle.load(f)
def _prepare_features(df: pd.DataFrame) -> np.ndarray:
    features = []
    for _, row in df.iterrows():
        log = row.to_dict()
        f = extract_features(log)[0]
        features.append(f)
    return np.array(features)