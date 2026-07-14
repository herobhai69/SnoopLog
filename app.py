import streamlit as st
import pandas as pd
from anomaly_engine import run_anomaly_engine

st.set_page_config(
    page_title="SnoopLog | Threat Center",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SnoopLog Intelligence Hub")
st.subheader("Unified Fraud & Cyber Anomaly Detection Engine")
st.markdown("---")


alerts = run_anomaly_engine()

total_threats = len(alerts)
high_risk_count = sum(1 for a in alerts if a['risk'] == 'High')
suspicious_count = sum(1 for a in alerts if a['risk'] == 'Suspicious')


col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Anomalies Detected", value=total_threats)
with col2:
    st.metric(label="🔴 High-Risk Incidents (Financial/Data)", value=high_risk_count)
with col3:
    st.metric(label="🟡 Suspicious Activity (Network/Login)", value=suspicious_count)

st.markdown("---")


st.header("🚨 Live Incident Response Feed")

if not alerts:
    st.success("System Secure: No active anomalies detected.")
else:
    for idx, alert in enumerate(alerts):
        alert_id = f"alert_{idx}"
        
        if alert['risk'] == "High":
            st.error(f"**CRITICAL THREAT** | Location: {alert['country']} ({alert['ip']}) | Device: {alert['device']}")
            st.markdown(f"**Triggered Rules:** {alert['message']}")
            
            c1, c2, _ = st.columns([1, 1, 6])
            with c1:
                if st.button("🚫 Freeze Account", key=f"freeze_{alert_id}"):
                    st.toast(f"Account associated with IP {alert['ip']} frozen.")
            with c2:
                if st.button("🔍 Investigate", key=f"inv_{alert_id}"):
                    st.toast(f"Incident report opened for {alert['ip']}.")
                    
        else:
            st.warning(f"**SUSPICIOUS ACTIVITY** | Location: {alert['country']} ({alert['ip']}) | Device: {alert['device']}")
            st.markdown(f"**Triggered Rules:** {alert['message']}")
            
            c1, _ = st.columns([1, 7])
            with c1:
                if st.button("Flag for Review", key=f"clear_{alert_id}"):
                    st.toast(f"Alert for IP {alert['ip']} flagged to Tier 1 support.")
                    
        st.markdown("---")