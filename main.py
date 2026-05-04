import time
from unittest import result
from ingestion.log_stream import generate_log
from core.pipeline import run_pipeline
from core.state import StateManager
from services.logger import log_event
from config import STREAM_INTERVAL
def main():
    print("🚀 AI Incident Response System Started\n")
    state_manager = StateManager()
    try:
        while True:
            log = generate_log()
            state = state_manager.get()
            result = run_pipeline(log, state)
            print("=" * 60)
            print(result)
            time.sleep(STREAM_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 System stopped gracefully")
log_event("incident", result)
if __name__ == "__main__":
    main()