import streamlit as st
from funcs.read_markdown import read_markdown_file

into_markdown = read_markdown_file('content/safeguarding/safeguarding officers/intro.md')

banner = "images/safeguarding/banner.png"
st.image(banner)
st.divider()

with st.container():
    st.markdown(into_markdown, unsafe_allow_html=True)
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Kirsty Lovell")   

    with right_col:
        st.subheader("Gemma Ryan")