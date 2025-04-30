import streamlit as st
import pandas as pd

st.title("📁 Upload Time Series Data")

uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.session_state.df = df
    st.write("Data preview:")
    st.dataframe(df.head())

    if st.button("Next: Train Model"):
        st.session_state.current_page = "2_Train"
        st.switch_page("pages/2_Train.py")