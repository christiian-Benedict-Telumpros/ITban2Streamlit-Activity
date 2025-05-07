II. DataFrame Viewer
This section focuses on displaying structured data—such as a CSV file—inside a Streamlit app. By combining Streamlit with the powerful data handling capabilities of Pandas, users can upload their own files and explore the data interactively.
The application begins by using st.file_uploader() to allow users to upload a CSV file. If no file is uploaded, a sample dataset is loaded using Python’s StringIO for demonstration purposes. This ensures the app remains functional even without user input.
Once the data is loaded, a checkbox (st.checkbox()) provides the user with the option to display the full raw dataset using st.dataframe(). This is helpful for quick inspection and exploration.
To make the data more interactive, a dropdown (st.selectbox()) is included, which allows users to filter the data based on the values in a specific column (in this case, "Department"). This filtered view helps users focus on relevant subsets of the data.
To ensure meaningful analysis, the uploaded file is expected to contain at least five columns, including a "Department" column used for filtering. If the required column is missing, the app displays a warning.
![image](https://github.com/user-attachments/assets/2272e5bc-401a-4b85-98ee-63867a8a463e)

![image](https://github.com/user-attachments/assets/e4f8c51d-30ef-49d5-af8d-e5ea613bbf03)
