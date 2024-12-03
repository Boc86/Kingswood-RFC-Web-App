import streamlit as st
from funcs.read_markdown import read_markdown_file

body_markdown = read_markdown_file('content/mental health/mental health/body.md')

banner = "images/mental health/banner.jpg"
st.image(banner)

with st.container():
    st.markdown(body_markdown, unsafe_allow_html=True)