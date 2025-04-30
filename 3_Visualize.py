import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Visualize Anomalies")

df = st.session_state.get("df")
scores = st.session_state.get("anomaly_scores")

if df is not None and scores is not None:
    fig, ax = plt.subplots()
    ax.plot(df.index, df.iloc[:, 1], label="Time Series")
    ax.plot(df.index, scores, label="Anomaly Score", color="red")
    ax.legend()
    st.pyplot(fig)

    if st.button("Next: Download Report"):
        st.session_state.current_page = "4_Download"
        st.switch_page("pages/4_Download.py")
else:
    st.warning("Train the model first.")