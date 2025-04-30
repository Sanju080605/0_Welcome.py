import streamlit as st

st.title("🤖 Train the Model")

df = st.session_state.get("df")

if df is not None:
    st.write("Uploaded Data Preview:")
    st.write(df.head())
    st.write(df.dtypes)

    numeric_cols = df.select_dtypes(include='number').columns

    if st.button("Start Training"):
        if len(numeric_cols) == 0:
            st.error("No numeric columns found in the dataset.")
        else:
            target_col = st.selectbox("Choose a numeric column for anomaly detection", numeric_cols)
            if target_col:
                st.session_state.anomaly_scores = df[target_col].rolling(window=5).std().fillna(0)
                st.success("✅ Training completed.")

    if "anomaly_scores" in st.session_state:
        if st.button("Next: Visualize"):
            st.session_state.current_page = "3_Visualize"
            st.switch_page("pages/3_Visualize.py")
else:
    st.warning("Please upload a dataset first.")
