import streamlit as st

banner = "images/parent info/banner.jpg"
st.image(banner)
st.header("👋 Welcome to the Kingswood Rugby Club!")
st.divider()

with st.container():

    lef_col, right_col = st.columns(2)

    with lef_col:
        st.markdown(open('content/parent info/welcome letter/body.txt').readlines())
    
    with right_col:
        st.subheader("Usefull Links")
        st.page_link("layout/Home/2 HowTo.py", label=None, icon=":material/help:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/parent info/2 Parent Volunteering.py", label=None, icon=":material/volunteer_activism:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Coaching/2 Coaching Team.py", label=None, icon=":material/diversity_2:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Safeguarding/1 Safeguarding.py", label=None, icon=":material/enhanced_encryption:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Mental Health/1 Mental Health.py", label=None, icon=":material/health_and_safety:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Policies/1 Policies.py", label=None, icon=":material/topic:", help=None, disabled=False, use_container_width=None)  