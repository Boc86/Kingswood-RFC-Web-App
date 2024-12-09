# This script creates a Streamlit app for the Athenas section of the Coaches Handbook

import streamlit as st
from funcs.read_markdown import read_markdown_file
from streamlit_pdf_viewer import pdf_viewer

# Read the markdown content for the intro section
intro_markdown = read_markdown_file('content/coaching/athenas/intro.md')

# Display the banner image for the coaching section
st.image("images/coaching/banner.png")

# Set the title of the page to "Coaches Handbook"
st.title("Coaches Handbook")

# Display the markdown content for the intro section
st.markdown(intro_markdown, unsafe_allow_html=True)

# Create 3 tabs for the different age groups
tab1, tab2, tab3 = st.tabs(["Under 16's", "Under 14's", "Under 12's"])

# Create an expander for the Under 16's section
with tab1:

    # Read the markdown content for the Under 16's section
    summary_markdown = read_markdown_file('content/coaching/athenas/under 16s/summary.md')
    training_markdown = read_markdown_file('content/coaching/athenas/under 16s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/athenas/under 16s/session plans.md')

     # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/athenas/under 16s/the kingswood way.pdf", width=500)

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/athenas/under 16s/info.png")

    # Create an expander for the Summary
    with st.expander("Summary", icon=":material/format_text_clip:"):
        # Display the markdown content for the Summary
        st.markdown(summary_markdown, unsafe_allow_html=True)

    # Create an expander for the Training Plan
    with st.expander("Training Plan", icon=":material/assignment:"):
        # Display the markdown content for the Training Plan
        st.markdown(training_markdown, unsafe_allow_html=True)

    # Create an expander for the Session Plans
    with st.expander("Session Plans", icon=":material/note_alt:"):
        # Display the markdown content for the Session Plans
        st.markdown(sessions_markdown, unsafe_allow_html=True)

# Create an expander for the Under 14's section
with tab2:

    # Read the markdown content for the Under 14's section
    summary_markdown = read_markdown_file('content/coaching/athenas/under 14s/summary.md')
    training_markdown = read_markdown_file('content/coaching/athenas/under 14s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/athenas/under 14s/session plans.md')

     # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/athenas/under 14s/the kingswood way.pdf", width=500)

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/athenas/under 14s/info.png")

    # Create an expander for the Summary
    with st.expander("Summary", icon=":material/format_text_clip:"):
        # Display the markdown content for the Summary
        st.markdown(summary_markdown, unsafe_allow_html=True)

    # Create an expander for the Training Plan
    with st.expander("Training Plan", icon=":material/assignment:"):
        # Display the markdown content for the Training Plan
        st.markdown(training_markdown, unsafe_allow_html=True)

    # Create an expander for the Session Plans
    with st.expander("Session Plans", icon=":material/note_alt:"):
        # Display the markdown content for the Session Plans
        st.markdown(sessions_markdown, unsafe_allow_html=True)

# Create an expander for the Under 12's section
with tab3:

    # Read the markdown content for the Under 12's section
    summary_markdown = read_markdown_file('content/coaching/athenas/under 12s/summary.md')
    training_markdown = read_markdown_file('content/coaching/athenas/under 12s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/athenas/under 12s/session plans.md')

     # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/athenas/under 12s/the kingswood way.pdf", width=500)

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/athenas/under 12s/info.png")

    # Create an expander for the Summary
    with st.expander("Summary", icon=":material/format_text_clip:"):
        # Display the markdown content for the Summary
        st.markdown(summary_markdown, unsafe_allow_html=True)

    # Create an expander for the Training Plan
    with st.expander("Training Plan", icon=":material/assignment:"):
        # Display the markdown content for the Training Plan
        st.markdown(training_markdown, unsafe_allow_html=True)

    # Create an expander for the Session Plans
    with st.expander("Session Plans", icon=":material/note_alt:"):
        # Display the markdown content for the Session Plans
        st.markdown(sessions_markdown, unsafe_allow_html=True)
