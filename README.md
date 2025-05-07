IV. Fetch and Display API Data
In this task, we demonstrate how to integrate live data from a public API—specifically, COVID-19 statistics—from the disease.sh API and visualize the information interactively using Streamlit widgets and data charts.
Steps and Features Implemented:

1. API Integration with requests:
A GET request is made to fetch country-wise COVID-19 statistics.
The JSON response is parsed into a Python dictionary and then converted to a Pandas DataFrame.

2.Data Cleaning & Preparation:
Key columns such as cases, deaths, recovered, etc., are selected.
Null values are filled, and all data types are coerced into numeric formats to prevent visualization issues.

3.Sidebar Filters:
Users can select one or more countries from a multiselect widget to filter the data.
If no countries are selected or the selected ones aren’t found, a fallback to default countries ensures continuity.

4. Interactive Data Display:
The filtered DataFrame is shown in a scrollable table using st.dataframe.

![image](https://github.com/user-attachments/assets/d71a1c33-6940-4543-be0a-e2866f4573b2)
![image](https://github.com/user-attachments/assets/6d3c4da9-8662-48ed-8bf2-2637733c515b)
