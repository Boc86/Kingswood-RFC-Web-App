import streamlit as st
from funcs.read_markdown import read_markdown_file

body_markdown = read_markdown_file('content/parent info/volunteering/body.md')

banner = "images/parent info/banner.jpg"
st.image(banner)
st.header("Volunteering")
st.divider()

with st.container():
    st.markdown(body_markdown, unsafe_allow_html=True)