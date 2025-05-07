V. Data Pipeline with Database (MySQL Integration)
1. Connect to a MySQL Database
The app uses SQLAlchemy to establish a connection to a MySQL database (task5telumpros).
Connection details like username, password, host, port, and database name are configured.

2. Fetch and Filter Data
A function (fetch_data) runs SQL queries to retrieve data from the database.
It supports using parameters (like filtering by username).

3. Display Data with st.dataframe
After a user logs in, their data is displayed using st.dataframe, which creates a table-like view in the Streamlit app.

4. Insert New Rows (Sign Up Form)
The sign-up form allows new users to register by entering a username, password, and email.
The password is hashed for security using the bcrypt library before it's stored in the database.

5. User Authentication (Bonus Feature)
Users can log in using their credentials.
The login process includes verifying that the password entered matches the hashed password stored in the database.
If the login is successful, the user is welcomed, and their data is shown.

![image](https://github.com/user-attachments/assets/694f8845-483e-42ca-9713-d16e9a57c16a)
![image](https://github.com/user-attachments/assets/b9cc58dc-ff5c-4935-a854-493a6c49b3b3)
![image](https://github.com/user-attachments/assets/fc95b2f6-1986-486d-9b82-b4aabb90eeac)
