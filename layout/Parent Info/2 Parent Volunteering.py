import streamlit as st

banner = "images/parent info/banner.jpg"
st.image(banner)
st.header("Volunteering")
st.divider()

with st.container():
    st.markdown(open('content/parent info/volunteering/body.txt').readlines())