import streamlit as st

st.title("🏢 Data Warehousing & Enterprise Data Management")

# Sidebar filters/options
st.sidebar.header("📌 Settings")
topic = st.sidebar.selectbox("Choose a topic:", [
    "Introduction", "ETL Process", "Data Marts", "Data Lakes", "Enterprise Data Management"
])
show_glossary = st.sidebar.checkbox("Show Glossary")

# Tabs to organize content
tab1, tab2 = st.tabs(["📘 Theory", "📊 Real-World Use"])

with tab1:
    st.subheader(f"📚 Topic: {topic}")
    
    if topic == "Introduction":
        st.write("A **Data Warehouse** is a central repository of integrated data from multiple sources.")
    elif topic == "ETL Process":
        st.write("**ETL (Extract, Transform, Load)** is the process of collecting data, transforming it into a standard format, and loading it into a data warehouse.")
    elif topic == "Data Marts":
        st.write("**Data Marts** are subsets of data warehouses tailored for specific departments like sales or finance.")
    elif topic == "Data Lakes":
        st.write("**Data Lakes** store raw, unstructured data that can be structured later for analysis.")
    elif topic == "Enterprise Data Management":
        st.write("**Enterprise Data Management (EDM)** involves policies, procedures, and standards for managing data across an organization.")

    # Optional expandable section
    with st.expander("📖 Learn more about Data Governance"):
        st.write("""
            Data Governance refers to the management of data availability, usability, integrity, and security.
            It's a key part of enterprise data management strategies.
        """)

with tab2:
    st.subheader("🌐 Example Use Cases")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Retail:**")
        st.write("Retail companies use data warehouses to analyze sales, customer trends, and inventory.")
    
    with col2:
        st.markdown("**Healthcare:**")
        st.write("Hospitals use data warehouses for patient record management and predictive diagnostics.")

# Sidebar glossary (optional)
if show_glossary:
    st.sidebar.markdown("### 📚 Glossary")
    st.sidebar.markdown("- **ETL**: Extract, Transform, Load")
    st.sidebar.markdown("- **EDM**: Enterprise Data Management")
    st.sidebar.markdown("- **OLAP**: Online Analytical Processing")
    st.sidebar.markdown("- **Data Mart**: Department-focused data subset")


