from navigation import make_sidebar
import streamlit as st

make_sidebar()

st.write(
    """
# 🔓 Dashboard

This is a secret page that only logged-in users can see.

Don't tell anyone.

For real.

"""
)