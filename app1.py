import streamlit as st
import pandas as pd
from io import StringIO

st.title("📊 Load and Display CSV Data")

# Provide sample CSV data
sample_csv = """
Name,Age,Gender,Department,Score
Alice,25,Female,HR,89
Bob,30,Male,Finance,76
Charlie,22,Male,IT,92
Diana,28,Female,Marketing,84
Evan,35,Male,HR,88
"""

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

# Load sample data if no file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("File successfully uploaded!")
else:
    st.info("No file uploaded. Using sample data for demonstration.")
    df = pd.read_csv(StringIO(sample_csv))

# Optional: view raw data
if st.checkbox("Show raw data"):
    st.dataframe(df)

# Selectbox to filter by a column
if "Department" in df.columns:
    department = st.selectbox("Select a department to filter", df["Department"].unique())
    filtered_data = df[df["Department"] == department]
    st.write(f"Filtered Data for Department: {department}")
    st.dataframe(filtered_data)
else:
    st.warning("The file must contain a 'Department' column to filter.")

