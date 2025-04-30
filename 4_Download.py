import streamlit as st

st.title("📥 Download Anomaly Report")

df = st.session_state.get("df")
scores = st.session_state.get("anomaly_scores")

if df is not None and scores is not None:
    df["Anomaly_Score"] = scores
    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button("⬇️ Download CSV", data=csv, file_name="anomaly_results.csv")

    st.success("🎉 You're done! Great work detecting anomalies.")
else:
    st.warning("Nothing to download.")