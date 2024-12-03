import streamlit as st

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(open('content/coaching/juniors/intro.txt').readlines())

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Colts", "Under 16's", "Under 15's", "Under 14's", "Under 13's"])

with tab1:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/colts/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/juniors/colts/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/juniors/colts/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/juniors/colts/session plans.txt").readlines())

with tab2:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 16s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/juniors/under 16s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/juniors/under 16s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/juniors/under 16s/session plans.txt").readlines())

with tab3:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 15s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/juniors/under 15s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/juniors/under 15s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/juniors/under 15s/session plans.txt").readlines())

with tab4:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 14s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/juniors/under 14s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/juniors/under 14s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/juniors/under 14s/session plans.txt").readlines())

with tab5:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 13s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/juniors/under 13s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/juniors/under 13s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/juniors/under 13s/session plans.txt").readlines())