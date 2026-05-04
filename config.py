import os
from dotenv import load_dotenv
load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
LLM_MODEL = os.getenv("LLM_MODEL", "mistral")

MODEL_DIR = "models"
ISOLATION_MODEL_PATH = os.path.join(MODEL_DIR, "isolation.pkl")

STREAM_INTERVAL = float(os.getenv("STREAM_INTERVAL", 1.0))
ANOMALY_THRESHOLD = float(os.getenv("ANOMALY_THRESHOLD", -0.2))