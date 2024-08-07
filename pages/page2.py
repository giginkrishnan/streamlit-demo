from navigation import make_sidebar
import streamlit as st
import pandas as pd
import numpy as np


make_sidebar()
data = pd.read_csv('./movies.csv')
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)
st.bar_chart(chart_data)
st.line_chart(chart_data)

st.write(data)