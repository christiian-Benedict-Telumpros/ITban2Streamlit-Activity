import streamlit as st
import pandas as pd
import requests
import altair as alt
import matplotlib.pyplot as plt

st.title("🦠 COVID-19 Global Stats Dashboard")

# Fetch data from public API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)
    df = df[["country", "cases", "todayCases", "deaths", "recovered", "active", "critical"]]

    # Handle NaN values by replacing them with 0
    df = df.fillna(0)

    # Ensure the columns are of the correct type (numeric)
    df["cases"] = pd.to_numeric(df["cases"], errors='coerce')
    df["todayCases"] = pd.to_numeric(df["todayCases"], errors='coerce')
    df["deaths"] = pd.to_numeric(df["deaths"], errors='coerce')
    df["recovered"] = pd.to_numeric(df["recovered"], errors='coerce')
    df["active"] = pd.to_numeric(df["active"], errors='coerce')
    df["critical"] = pd.to_numeric(df["critical"], errors='coerce')

    # Sidebar: select countries to display
    countries = st.sidebar.multiselect("🌍 Select countries to view", df["country"].unique(), default=["USA", "India", "Brazil"])

    # Check if the selected countries exist in the data and set default if not
    selected_countries = [country for country in countries if country in df["country"].values]
    if not selected_countries:
        selected_countries = df["country"].head(3).tolist()  # Default to the first 3 countries if none selected
    
    filtered_df = df[df["country"].isin(selected_countries)]

    st.subheader("📊 COVID-19 Cases by Country")
    st.dataframe(filtered_df)

    # 1. Bar Chart – Total Cases
    st.markdown("### 🟥 Bar Chart: Total Cases")
    bar_chart = alt.Chart(filtered_df).mark_bar().encode(
        x='country',
        y='cases',
        color='country'
    )
    st.altair_chart(bar_chart, use_container_width=True)

    # 2. Line Chart – Active vs Critical
    st.markdown("### 🔵 Line Chart: Active vs Critical")
    line_data = filtered_df.melt(id_vars="country", value_vars=["active", "critical"])
    line_chart = alt.Chart(line_data).mark_line(point=True).encode(
        x='country:N',
        y='value:Q',
        color='variable:N'
    )
    st.altair_chart(line_chart, use_container_width=True)

    # 3. Area Chart – Deaths
    st.markdown("### 🟡 Area Chart: Deaths")
    area_chart = alt.Chart(filtered_df).mark_area(opacity=0.5).encode(
        x='country',
        y='deaths',
        color='country'
    )
    st.altair_chart(area_chart, use_container_width=True)

    # 4. Pie Chart – Today's Cases
    st.markdown("### 🟢 Pie Chart: Today’s Cases")
    
    if not filtered_df["todayCases"].isnull().all() and filtered_df["todayCases"].sum() > 0:
        fig, ax = plt.subplots()
        ax.pie(filtered_df["todayCases"], labels=filtered_df["country"], autopct="%1.1f%%")
        ax.axis("equal")  # Equal aspect ratio ensures that pie chart is circular.
        st.pyplot(fig)
    else:
        st.warning("No data available to display in the pie chart.")

    # 5. Bar Chart (Horizontal) – Recovered
    st.markdown("### 🟣 Horizontal Bar Chart: Recovered")
    st.bar_chart(filtered_df.set_index("country")["recovered"])

else:
    st.error("Failed to fetch data from API.")
