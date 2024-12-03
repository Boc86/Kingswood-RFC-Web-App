import streamlit as st
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/coaching/juniors/intro.md')

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(intro_markdown, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Colts", "Under 16's", "Under 15's", "Under 14's", "Under 13's"])

with tab1:

    summary_markdown = read_markdown_file('content/coaching/juniors/colts/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/colts/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/colts/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/colts/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab2:

    summary_markdown = read_markdown_file('content/coaching/juniors/under 16s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 16s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 16s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 16s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab3:

    summary_markdown = read_markdown_file('content/coaching/juniors/under 15s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 15s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 15s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 15s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab4:

    summary_markdown = read_markdown_file('content/coaching/juniors/under 14s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 14s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 14s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 14s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab5:

    summary_markdown = read_markdown_file('content/coaching/juniors/under 13s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 13s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 13s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/juniors/under 13s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)