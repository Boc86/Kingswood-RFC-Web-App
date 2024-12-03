import streamlit as st
from funcs.read_markdown import read_markdown_file

body_markdown = read_markdown_file('content/safeguarding/safeguarding/body.md')

banner = "images/safeguarding/banner.png"
st.image(banner)
st.divider()

with st.container():
    st.markdown(body_markdown, unsafe_allow_html=True)