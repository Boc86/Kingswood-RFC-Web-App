import streamlit as st
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/coaching/athenas/intro.md')

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(intro_markdown, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Under 16's", "Under 14's", "Under 12's"])

with tab1:

    summary_markdown = read_markdown_file('content/coaching/athenas/under 16s/summary.md')
    training_markdown = read_markdown_file('content/coaching/athenas/under 16s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/athenas/under 16s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/athenas/under 16s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab2:

    summary_markdown = read_markdown_file('content/coaching/athenas/under 14s/summary.md')
    training_markdown = read_markdown_file('content/coaching/athenas/under 14s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/athenas/under 14s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/athenas/under 14s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab3:

    summary_markdown = read_markdown_file('content/coaching/athenas/under 12s/summary.md')
    training_markdown = read_markdown_file('content/coaching/athenas/under 12s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/athenas/under 12s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/athenas/under 12s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)