from ingestion.log_stream import generate_log
def simulate_batch(n=10):
    return [generate_log() for _ in range(n)]