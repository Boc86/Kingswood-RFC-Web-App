import streamlit as st

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(open('content/coaching/athenas/intro.txt').readlines())

tab1, tab2, tab3 = st.tabs(["Under 16's", "Under 14's", "Under 12's"])

with tab1:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/athenas/under 16s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/athenas/under 16s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/athenas/under 16s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/athenas/under 16s/session plans.txt").readlines())

with tab2:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/athenas/under 14s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/athenas/under 14s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/athenas/under 14s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/athenas/under 14s/session plans.txt").readlines())

with tab3:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/athenas/under 12s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/athenas/under 12s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/athenas/under 12s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/athenas/under 12s/session plans.txt").readlines())