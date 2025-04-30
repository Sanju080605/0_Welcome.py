import streamlit as st

st.set_page_config(page_title="Welcome", page_icon="👋")

st.title("👋 Welcome to Time Series Anomaly Detector")
st.markdown("""
This app lets you detect anomalies in your time series data using Transformer models.

Steps:
1. Upload your CSV file
2. Train the model
3. Visualize anomalies
4. Download the results
""")

if st.button("🚀 Get Started"):
    st.session_state.current_page = "1_Upload"
    st.switch_page("pages/1_Upload.py")