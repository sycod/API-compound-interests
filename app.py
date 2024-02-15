"""Streamlit simple GUI"""

import plotly.express as px
import streamlit as st
import yaml

with open('config.yaml', 'r') as f:
    ma_config = yaml.safe_load(f)

rate = ma_config["rate"]
initial_k = ma_config["initial_k"]
ann_savings = ma_config["ann_savings"]

st.header("Un last test")
st.subheader(f"My initial capital is {initial_k}")


df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)
