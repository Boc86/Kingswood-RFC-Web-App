import streamlit as st
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/mental health/resources/intro.md')

banner = "images/mental health/banner.jpg"
st.image(banner)

with st.container():
    st.markdown(intro_markdown, unsafe_allow_html=True)