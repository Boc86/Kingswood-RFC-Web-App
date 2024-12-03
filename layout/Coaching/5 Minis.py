import streamlit as st
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/coaching/minis/intro.md')

st.image("images/coaching/banner.png")
st.title("Coaches Handbook")
st.markdown(intro_markdown, unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Under 12's", "Under 11's", "Under 10's", "Under 9's", "Under 8's", "Under 7's", "Micros"])

with tab1:

    summary_markdown = read_markdown_file('content/coaching/minis/under 12s/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/under 12s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/under 12s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 12s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab2:

    summary_markdown = read_markdown_file('content/coaching/minis/under 11s/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/under 11s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/under 11s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 11s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab3:

    summary_markdown = read_markdown_file('content/coaching/minis/under 10s/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/under 10s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/under 10s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 10s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab4:

    summary_markdown = read_markdown_file('content/coaching/minis/under 9s/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/under 9s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/under 9s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 9s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab5:

    summary_markdown = read_markdown_file('content/coaching/minis/under 8s/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/under 8s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/under 8s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 8s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab6:

    summary_markdown = read_markdown_file('content/coaching/minis/under 7s/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/under 7s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/under 7s/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/under 7s/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)

with tab7:

    summary_markdown = read_markdown_file('content/coaching/minis/micros/summary.md')
    training_markdown = read_markdown_file('content/coaching/minis/micros/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/minis/micros/session plans.md')

    with st.expander("Infographic", icon=":material/info:"):
        st.image("content/coaching/minis/micros/info.png")
    with st.expander("Summary", icon=":material/format_text_clip:"):
        st.markdown(summary_markdown, unsafe_allow_html=True)
    with st.expander("Training Plan", icon=":material/assignment:"):
        st.markdown(training_markdown, unsafe_allow_html=True)
    with st.expander("Session Plans", icon=":material/note_alt:"):
        st.markdown(sessions_markdown, unsafe_allow_html=True)