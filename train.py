import pandas as pd
from ingestion.preprocessing import preprocess_log
from detectors.features import extract_features
from detectors.isolation import train_isolation
print("📥 Loading logs...")
df = pd.read_csv("data/logs.csv")
print("🧹 Preprocessing logs...")
processed_logs = []
for _, row in df.iterrows():
    log = preprocess_log(row.to_dict())
    processed_logs.append(log)
df_processed = pd.DataFrame(processed_logs)
if df_processed.empty:
    raise Exception("❌ No valid data after preprocessing")
print(f"✅ Processed {len(df_processed)} logs")
print(df_processed["action"].value_counts())
train_isolation(df_processed)
print("🚀 Training complete")