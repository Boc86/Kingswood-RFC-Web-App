import streamlit as st
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/home/external links/intro.md')
body_markdown = read_markdown_file('content/home/external links/body.md')

banner = "images/home/banner.jpg"
st.image(banner)

with st.container():
    st.markdown(intro_markdown, unsafe_allow_html=True)

with st.container():
    st.markdown(body_markdown, unsafe_allow_html=True)