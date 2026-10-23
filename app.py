import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dengue Dashboard",
    page_icon="🦟",
    layout="wide"
)

st.title("🦟 AI-Based Dengue Data Analysis Dashboard")
st.write("Explore and analyze dengue data.")

uploaded_file = st.file_uploader(
    "Upload your Dengue CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df.head(10))

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Rows", len(df))

    with col2:
        st.metric("Total Columns", len(df.columns))

    st.subheader("Dataset Information")
    st.write("Column Names:", list(df.columns))

    st.subheader("Numerical Data Analysis")
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:
        selected_column = st.selectbox(
            "Select a column",
            numeric_columns
        )

        st.line_chart(df[selected_column])
        st.bar_chart(df[selected_column])
    else:
        st.info("No numerical columns found.")

else:
    st.info("Upload your Dengue_EDA.csv file to view the dashboard.")
