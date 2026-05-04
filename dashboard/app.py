import streamlit as st
import pandas as pd
import time
from ingestion.log_stream import generate_log
from core.pipeline import run_pipeline
from core.state import StateManager
st.set_page_config(
    page_title="AI Incident Response",
    layout="wide",
    page_icon="🚨"
)
st.markdown("""
<style>
.card {
    padding: 12px;
    border-radius: 10px;
    background: #161b22;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)
if "history" not in st.session_state:
    st.session_state.history = []
if "running" not in st.session_state:
    st.session_state.running = False
if "state_manager" not in st.session_state:
    st.session_state.state_manager = StateManager()
st.title("🚨 AI Incident Response Dashboard")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("▶ Start"):
        st.session_state.running = True
with col2:
    if st.button("⏸ Stop"):
        st.session_state.running = False
with col3:
    if st.button("🧹 Reset"):
        st.session_state.history = []
if st.session_state.running:
    log = generate_log()
    state = st.session_state.state_manager.get()
    result = run_pipeline(log, state)
    st.session_state.state_manager.update(log["user"], log)
    st.session_state.history.append(result)
    st.session_state.history = st.session_state.history[-100:]
    time.sleep(0.5)
    st.rerun()
df = pd.DataFrame(st.session_state.history)
st.subheader("🔎 Filters")
level_filter = st.multiselect(
    "Risk Level",
    ["low", "medium", "high", "critical"],
    default=["high", "critical"]
)
if not df.empty:
    df_filtered = df[df["risk_level"].isin(level_filter)]
else:
    df_filtered = df
st.subheader("📊 Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Logs", len(df))
col2.metric("High Risk", len(df[df["risk_level"] == "high"]))
col3.metric("Critical", len(df[df["risk_level"] == "critical"]))
st.subheader("📋 Activity")
if not df_filtered.empty:
    st.dataframe(
        df_filtered.sort_values(by="risk_score", ascending=False),
        use_container_width=True
    )
st.subheader("🚨 Alerts")
for r in reversed(st.session_state.history):
    if r["risk_level"] in ["high", "critical"]:
        st.markdown(f"""
        <div class="card">
        <b>{r['incident_id']}</b> | {r['user']}<br>
        Risk: <b>{r['risk_level'].upper()}</b> ({r['risk_score']})<br>
        {r['summary']}
        </div>
        """, unsafe_allow_html=True)
st.subheader("🔍 Investigation")
if st.session_state.history:
    selected = st.selectbox(
        "Select Incident",
        st.session_state.history,
        format_func=lambda x: x["incident_id"]
    )
    st.json(selected)