import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(
    page_title="AI Workflow Report",
    layout="wide"
)

# Title
st.title("📊 AI Workflow & Report Generator")

st.write(
    "Upload a CSV file and generate AI-based business reports instantly."
)

# Sidebar
st.sidebar.title("Menu")
st.sidebar.info("Upload data and generate reports")

# File uploader
uploaded_file = st.file_uploader(
    "📂 Upload CSV File",
    type=["csv"]
)

# If file uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Buttons
    st.subheader("⚡ Generate Report")

    col1, col2, col3 = st.columns(3)

    with col1:
        trend_btn = st.button("📈 Trends")

    with col2:
        anomaly_btn = st.button("🚨 Anomalies")

    with col3:
        action_btn = st.button("🎯 Business Actions")

    # Outputs
    if trend_btn:
        st.success("📈 The data shows a stable overall trend.")

    if anomaly_btn:
        st.warning("🚨 Some unusual values have been detected in the dataset.")

    if action_btn:
        st.info("""
        🎯 Recommended Business Actions:
        1. Analyze periods with low performance  
        2. Investigate the causes of detected anomalies  
        3. Focus resources on high-performing areas  
        """)

else:
    st.warning("⚠️ Please upload a CSV file to continue.")

# Limitations
st.divider()
st.caption(
    "Note: AI-generated insights are for guidance only and should not be considered final decisions."
)
