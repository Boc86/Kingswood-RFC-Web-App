import streamlit as st

banner = "images/safeguarding/banner.png"
st.image(banner)
st.divider()

with st.container():
    st.markdown(open('content/safeguarding/safeguarding officers/intro.txt').readlines())
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Kirsty Lovell")   

    with right_col:
        st.subheader("Gemma Ryan")