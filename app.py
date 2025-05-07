import streamlit as st

# Basic text elements
st.title("Hello, Streamlit!")
st.header("🎯 Getting Started with Streamlit")
st.write("This simple app shows how to take user input and display output.")

# Input fields
name = st.text_input("What's your name?")
age = st.number_input("How old are you?", min_value=0, max_value=120, step=1)

# Display output based on input
if name:
    st.write(f"👋 Hello, **{name}**!")
    st.write(f"🎂 You are **{int(age)}** years old.")