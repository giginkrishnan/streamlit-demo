import streamlit as st
from time import sleep
# from navigation import make_sidebar

# make_sidebar()

def login():
    st.title("Welcome to GGNLIVE")

    st.write("Please log in to continue (username `test`, password `test`).")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log in", type="primary"):
        if username == "test" and password == "test":
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/page1.py")
        else:
            st.error("Incorrect username or password")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/page1.py")
else:
    login()