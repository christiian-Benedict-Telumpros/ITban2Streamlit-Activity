import streamlit as st
from sqlalchemy import create_engine, text
import pandas as pd
import bcrypt

# MySQL connection details
USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '3306'
DATABASE = 'task5telumpros'
DATABASE_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL)

def fetch_data(query, params=None):
    """Fetch data from database using SQLAlchemy."""
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn, params=params)

def hash_password(password):
    """Hash the password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_password(password, hashed):
    """Check if the entered password matches the stored hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

# Streamlit UI Setup
st.title("User Auth System (with Bonus Points 😎)")

page = st.radio("Choose an option", ["Login", "Sign Up", "View Users"])

# ========================= LOGIN FORM =========================
if page == "Login":
    st.subheader("Login")
    with st.form(key="login_form"):
        username_input = st.text_input("Username")
        password_input = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    if login_button:
        # SQL query to check the username
        query = "SELECT * FROM users WHERE username = :username"
        result = fetch_data(query, {"username": username_input})

        # Check if the result is found and validate password
        if len(result) > 0 and check_password(password_input, result.iloc[0]['password']):
            st.success("✅ Login successful!")

            # Show user data (username and email) only after login
            st.subheader("Welcome!")
            st.write(f"Username: {result.iloc[0]['username']}")
            st.write(f"Email: {result.iloc[0]['email']}")

            # After login, display a data frame with the user-specific data (optional)
            # For example, fetch user-specific data from the database (if applicable)
            user_data_query = "SELECT * FROM users WHERE username = :username"
            user_data = fetch_data(user_data_query, {"username": username_input})

            st.subheader("User Data")
            st.dataframe(user_data)  # This will display the user's data

        else:
            st.error("❌ Invalid username or password.")

# ========================= SIGN-UP FORM =========================
elif page == "Sign Up":
    st.subheader("Create an Account")
    with st.form(key="signup_form"):
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        new_email = st.text_input("Email")
        signup_button = st.form_submit_button("Sign Up")

    if signup_button:
        # Check if username already exists
        check_query = "SELECT * FROM users WHERE username = :username"
        check_result = fetch_data(check_query, {"username": new_username})

        if len(check_result) > 0:
            st.warning("Username already exists. Try another.")
        else:
            # Hash the password before storing it
            hashed_pw = hash_password(new_password)

            # Insert new user into the database
            insert_query = """
                INSERT INTO users (username, password, email)
                VALUES (:username, :password, :email)
            """
            params = {
                "username": new_username,
                "password": hashed_pw,
                "email": new_email
            }
            with engine.begin() as conn:
                conn.execute(text(insert_query), params)
            st.success("🎉 Account created! You can now log in.")

# ========================= VIEW USERS =========================
elif page == "View Users":
    st.subheader("List of Users")
    query = "SELECT username, email FROM users"  # Query to select all users
    users_data = fetch_data(query)

    if len(users_data) > 0:
        st.dataframe(users_data)  # Display the fetched data in a table format
    else:
        st.warning("No users found.")
