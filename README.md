I. Hello, Streamlit!
This section introduces the basic components of a Streamlit application. Streamlit is an open-source Python library that allows users to create interactive web applications quickly and easily. It is especially popular for data science and machine learning projects due to its simplicity and speed.
To begin, we install Streamlit using the command pip install streamlit. After installation, we create a Python file (commonly named app.py) that contains the logic and layout of our app.
Within this file, we use Streamlit functions to add content to the page. The st.title() function displays the main title of the app, while st.header() is used for section headings. The st.write() function is a versatile method for displaying text, variables, and even dataframes.
To make the app interactive, we include input fields such as st.text_input() for receiving text from users, and st.number_input() for numerical input. Based on the input provided by the user, we can generate dynamic output—showing results or performing calculations using Streamlit's reactive framework.
This foundational exercise helps users understand how to build a simple interactive interface using just Python—no need for HTML, CSS, or JavaScript.
![image](https://github.com/user-attachments/assets/1c5a88dd-ee65-4adc-839a-95d4ce53bf1f)

II. DataFrame Viewer
This section focuses on displaying structured data—such as a CSV file—inside a Streamlit app. By combining Streamlit with the powerful data handling capabilities of Pandas, users can upload their own files and explore the data interactively.
The application begins by using st.file_uploader() to allow users to upload a CSV file. If no file is uploaded, a sample dataset is loaded using Python’s StringIO for demonstration purposes. This ensures the app remains functional even without user input.
Once the data is loaded, a checkbox (st.checkbox()) provides the user with the option to display the full raw dataset using st.dataframe(). This is helpful for quick inspection and exploration.
To make the data more interactive, a dropdown (st.selectbox()) is included, which allows users to filter the data based on the values in a specific column (in this case, "Department"). This filtered view helps users focus on relevant subsets of the data.
To ensure meaningful analysis, the uploaded file is expected to contain at least five columns, including a "Department" column used for filtering. If the required column is missing, the app displays a warning.
![image](https://github.com/user-attachments/assets/ed477d86-a082-48b0-a7b8-81e1dc3ec4b2)

III. Sidebar and Layout
This section demonstrates how to design a user-friendly and organized layout in a Streamlit application. The example focuses on Data Warehousing and Enterprise Data Management (EDM)—two essential concepts in large-scale data systems.
The sidebar, created using st.sidebar, acts as a control panel where users can select different topics from a dropdown (st.selectbox) and optionally display a glossary using a checkbox. This design pattern keeps the main page clean while allowing users to easily navigate or modify the view.
To better separate content, the app uses st.tabs() to create two logical sections:
Theory: Contains educational information about data warehousing concepts.
Real-World Use: Provides industry-specific use cases (e.g., retail and healthcare) presented side-by-side using st.columns().
An additional layout component, st.expander(), is used within the Theory tab. It hides in-depth information on Data Governance, which users can optionally expand to read more—supporting a cleaner and more interactive user experience.

Lastly, if the user enables the "Show Glossary" option from the sidebar, Streamlit displays a glossary of relevant terms such as ETL, EDM, OLAP, and Data Mart. This is especially useful for beginners or viewers unfamiliar with technical terms.
![image](https://github.com/user-attachments/assets/4e9a67e7-5d44-421c-9dd4-db6109b69467)

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
![image](https://github.com/user-attachments/assets/858bb644-8730-4efa-a292-f7e6d4b5e6fb)

V. Data Pipeline with Database (MySQL Integration)
