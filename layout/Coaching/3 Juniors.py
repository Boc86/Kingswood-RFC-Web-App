# This file contains the layout for the Juniors section of the Coaches Handbook 

import streamlit as st
from funcs.read_markdown import read_markdown_file
from streamlit_pdf_viewer import pdf_viewer

# Read the introductory markdown content for the Coaches Handbook
intro_markdown = read_markdown_file('content/coaching/juniors/intro.md')

# Display the banner image for the coaching section
st.image("images/coaching/banner.png")

# Set the title of the page to "Coaches Handbook"
st.title("Coaches Handbook")

# Display the markdown content on the page, allowing HTML if present
st.markdown(intro_markdown, unsafe_allow_html=True)

# Create a horizontal tabs container with 5 tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Colts", "Under 16's", "Under 15's", "Under 14's", "Under 13's"])

# Create a container for the Colts section
with tab1:
    # Read the markdown content for the Colts section

    summary_markdown = read_markdown_file('content/coaching/juniors/colts/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/colts/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/colts/session plans.md')

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/juniors/colts/info.png")

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

# Create a container for the Under 16's section
with tab2:
    # Read the markdown content for the Under 16's section
    summary_markdown = read_markdown_file('content/coaching/juniors/under 16s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 16s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 16s/session plans.md')

     # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/juniors/under 16s/the kingswood way.pdf", width=500)

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/juniors/under 16s/info.png")

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

# Create a container for the Under 15's section
with tab3:
    # Read the markdown content for the Under 15's section
    summary_markdown = read_markdown_file('content/coaching/juniors/under 15s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 15s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 15s/session plans.md')

     # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/juniors/under 15s/the kingswood way.pdf", width=500)

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/juniors/under 15s/info.png")

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

# Create a container for the Under 14's section
with tab4:
    # Read the markdown content for the Under 14's section
    summary_markdown = read_markdown_file('content/coaching/juniors/under 14s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 14s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 14s/session plans.md')
    
    # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/juniors/under 14s/the kingswood way.pdf", width=500)

    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/juniors/under 14s/info.png")

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

# Create a container for the Under 13's section
with tab5:
    # Read the markdown content for the Under 13's section
    summary_markdown = read_markdown_file('content/coaching/juniors/under 13s/summary.md')
    training_markdown = read_markdown_file('content/coaching/juniors/under 13s/training plan.md')
    sessions_markdown = read_markdown_file('content/coaching/juniors/under 13s/session plans.md')

    # Create an expander for the kingswood way
    with st.expander("The Kingswood Way", icon=":material/forest:"):
        # Display the content
        pdf_viewer("content/coaching/juniors/under 13s/the kingswood way.pdf", width=500)
    
    # Create an expander for the Infographic
    with st.expander("Infographic", icon=":material/info:"):
        # Display the infographic image
        st.image("content/coaching/juniors/under 13s/info.png")

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
