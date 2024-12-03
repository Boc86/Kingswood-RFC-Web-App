import streamlit as st

st.image("images/coaching/banner.png")
st.title("Resources")

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Coaching Drills")

with right_col:
    st.subheader("Game Tactics")