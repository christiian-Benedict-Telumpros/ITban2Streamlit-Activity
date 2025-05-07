I. Hello, Streamlit!
This section introduces the basic components of a Streamlit application. Streamlit is an open-source Python library that allows users to create interactive web applications quickly and easily. It is especially popular for data science and machine learning projects due to its simplicity and speed.

To begin, we install Streamlit using the command pip install streamlit. After installation, we create a Python file (commonly named app.py) that contains the logic and layout of our app.

Within this file, we use Streamlit functions to add content to the page. The st.title() function displays the main title of the app, while st.header() is used for section headings. The st.write() function is a versatile method for displaying text, variables, and even dataframes.

To make the app interactive, we include input fields such as st.text_input() for receiving text from users, and st.number_input() for numerical input. Based on the input provided by the user, we can generate dynamic output—showing results or performing calculations using Streamlit's reactive framework.

This foundational exercise helps users understand how to build a simple interactive interface using just Python—no need for HTML, CSS, or JavaScript.
