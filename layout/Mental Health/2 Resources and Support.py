import streamlit as st
from streamlit.components.v1 import iframe

banner = "images/mental health/banner.jpg"
st.image(banner)

with st.container():
    st.markdown(open('content/mental health/resources/intro.txt').readlines())