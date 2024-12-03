import streamlit as st
from funcs.read_markdown import read_markdown_file

body_markdown = read_markdown_file('content/home/home/body.md')

banner = "images/home/banner.jpg"
st.image(banner)

with st.container():
    st.header("👋 Welcome to the Kingswood Rugby Club Volunteers Community!")
    st.markdown(body_markdown, unsafe_allow_html=True)

with st.container():
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Usefull Links")
        st.page_link("layout/Home/2 HowTo.py", label=None, icon=":material/help:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Parent Info/1 Parent Info.py", label=None, icon=":material/info:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Player Info/1 Player Info.py", label=None, icon=":material/info:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Coaching/2 Coaching Team.py", label=None, icon=":material/diversity_2:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Safeguarding/1 Safeguarding.py", label=None, icon=":material/enhanced_encryption:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Mental Health/1 Mental Health.py", label=None, icon=":material/health_and_safety:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Policies/1 Policies.py", label=None, icon=":material/topic:", help=None, disabled=False, use_container_width=None)  
    
    with right_col:
        st.empty()