import streamlit as st

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(open("content/coaching/coaches handbook/intro.txt").readlines())

with st.container():
    st.write("---")

    st.subheader("Usefull Links")
    st.page_link("layout/Coaching/2 Coaching Team.py", label=None, icon=":material/diversity_2:", help=None, disabled=False, use_container_width=None)
    st.page_link("layout/Coaching/3 Juniors.py", label=None, icon=":material/man:", help=None, disabled=False, use_container_width=None)
    st.page_link("layout/Coaching/4 Athenas.py", label=None, icon=":material/woman:", help=None, disabled=False, use_container_width=None)
    st.page_link("layout/Coaching/5 Minis.py", label=None, icon=":material/boy:", help=None, disabled=False, use_container_width=None)
    st.page_link("layout/Coaching/6 Resources.py", label=None, icon=":material/share:", help=None, disabled=False, use_container_width=None)