import streamlit as st

banner = "images/safeguarding/banner.png"
st.image(banner)
st.divider()

with st.container():
    st.markdown(open('content/safeguarding/safeguarding policy/body.txt').readlines())