from navigation import make_sidebar
import streamlit as st
import pandas as pd

make_sidebar()
data = pd.read_csv('./movies.csv')
st.write(data)