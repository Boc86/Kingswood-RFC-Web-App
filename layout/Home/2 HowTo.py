import streamlit as st
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/home/how to/intro.md')
tab1_markdown = read_markdown_file('content/home/how to/tab1.md')
tab2_markdown = read_markdown_file('content/home/how to/tab2.md')
tab3_markdown = read_markdown_file('content/home/how to/tab3.md')

banner = "images/home/banner.jpg"
st.image(banner)

with st.container():
    st.markdown(intro_markdown, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Navigation", "Contribute", "Discussion"])

    tab1.markdown(tab1_markdown, unsafe_allow_html=True)
    
    tab2.markdown(tab2_markdown, unsafe_allow_html=True)
    
    tab3.markdown(tab3_markdown, unsafe_allow_html=True)
    