import streamlit as st

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(open('content/coaching/minis/intro.txt').readlines())

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Under 12's", "Under 11's", "Under 10's", "Under 9's", "Under 8's", "Under 7's", "Micros"])

with tab1:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 12s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/under 12s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/under 12s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/under 12s/session plans.txt").readlines())

with tab2:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 11s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/under 11s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/under 11s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/under 11s/session plans.txt").readlines())

with tab3:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 10s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/under 10s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/under 10s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/under 10s/session plans.txt").readlines())

with tab4:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 9s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/under 9s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/under 9s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/under 9s/session plans.txt").readlines())

with tab5:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 8s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/under 8s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/under 8s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/under 8s/session plans.txt").readlines())

with tab6:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 7s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/under 7s/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/under 7s/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/under 7s/session plans.txt").readlines())

with tab7:
    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/micros/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(open("content/coaching/minis/micros/summary.txt").readlines())
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(open("content/coaching/minis/micros/training plan.txt").readlines())
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(open("content/coaching/minis/micros/session plans.txt").readlines())