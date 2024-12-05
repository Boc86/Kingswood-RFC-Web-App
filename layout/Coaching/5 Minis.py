# This file contains the layout for the Minis section of the Coaching Handbook.

import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read the markdown content for the intro to the Minis section
intro_markdown = read_markdown_file('content/coaching/minis/intro.md')

# Display the banner image for the Minis section
st.image("images/coaching/banner.png")

# Set the title of the page to "Coaches Handbook"
st.title("Coaches Handbook")

# Display the markdown content for the intro to the Minis section
st.markdown(intro_markdown, unsafe_allow_html=True)

# Create a list of tabs for the different age groups in the Minis section
tabs = [
    "Under 12's",
    "Under 11's",
    "Under 10's",
    "Under 9's",
    "Under 8's",
    "Under 7's",
    "Micros"
]

# Create a list to hold the tabs
tab_list = []

# Loop over the tabs and create a tab for each one
for tab in tabs:
    tab_list.append(st.tab(tab))

# Create a variable to hold the current tab
current_tab = 0

# Loop over the tabs and display the content for each one
for tab in tab_list:
    with tab:
        if current_tab == 0:
            # Read the markdown content for the Under 12's section
            summary_markdown = read_markdown_file('content/coaching/minis/under 12s/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/under 12s/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/under 12s/session plans.md')

            # Display the infographic for the Under 12's section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/under 12s/info.png")

            # Display the summary for the Under 12's section
            with st.expander("Summary", icon=":material/format_text_clip:"):
                st.markdown(summary_markdown, unsafe_allow_html=True)

            # Display the training plan for the Under 12's section
            with st.expander("Training Plan", icon=":material/assignment:"):
                st.markdown(training_markdown, unsafe_allow_html=True)

            # Display the session plans for the Under 12's section
            with st.expander("Session Plans", icon=":material/note_alt:"):
                st.markdown(sessions_markdown, unsafe_allow_html=True)
        elif current_tab == 1:
            # Read the markdown content for the Under 11's section
            summary_markdown = read_markdown_file('content/coaching/minis/under 11s/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/under 11s/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/under 11s/session plans.md')

            # Display the infographic for the Under 11's section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/under 11s/info.png")

            # Display the summary for the Under 11's section
            with st.expander("Summary", icon=":material/format_text_clip:"):
                st.markdown(summary_markdown, unsafe_allow_html=True)

            # Display the training plan for the Under 11's section
            with st.expander("Training Plan", icon=":material/assignment:"):
                st.markdown(training_markdown, unsafe_allow_html=True)

            # Display the session plans for the Under 11's section
            with st.expander("Session Plans", icon=":material/note_alt:"):
                st.markdown(sessions_markdown, unsafe_allow_html=True)
        elif current_tab == 2:
            # Read the markdown content for the Under 10's section
            summary_markdown = read_markdown_file('content/coaching/minis/under 10s/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/under 10s/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/under 10s/session plans.md')

            # Display the infographic for the Under 10's section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/under 10s/info.png")

            # Display the summary for the Under 10's section
            with st.expander("Summary", icon=":material/format_text_clip:"):
                st.markdown(summary_markdown, unsafe_allow_html=True)

            # Display the training plan for the Under 10's section
            with st.expander("Training Plan", icon=":material/assignment:"):
                st.markdown(training_markdown, unsafe_allow_html=True)

            # Display the session plans for the Under 10's section
            with st.expander("Session Plans", icon=":material/note_alt:"):
                st.markdown(sessions_markdown, unsafe_allow_html=True)
        elif current_tab == 3:
            # Read the markdown content for the Under 9's section
            summary_markdown = read_markdown_file('content/coaching/minis/under 9s/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/under 9s/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/under 9s/session plans.md')

            # Display the infographic for the Under 9's section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/under 9s/info.png")

            # Display the summary for the Under 9's section
            with st.expander("Summary", icon=":material/format_text_clip:"):
                st.markdown(summary_markdown, unsafe_allow_html=True)

            # Display the training plan for the Under 9's section
            with st.expander("Training Plan", icon=":material/assignment:"):
                st.markdown(training_markdown, unsafe_allow_html=True)

            # Display the session plans for the Under 9's section
            with st.expander("Session Plans", icon=":material/note_alt:"):
                st.markdown(sessions_markdown, unsafe_allow_html=True)
        elif current_tab == 4:
            # Read the markdown content for the Under 8's section
            summary_markdown = read_markdown_file('content/coaching/minis/under 8s/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/under 8s/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/under 8s/session plans.md')

            # Display the infographic for the Under 8's section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/under 8s/info.png")

            # Display the summary for the Under 8's section
            with st.expander("Summary", icon=":material/format_text_clip:"):
                st.markdown(summary_markdown, unsafe_allow_html=True)

            # Display the training plan for the Under 8's section
            with st.expander("Training Plan", icon=":material/assignment:"):
                st.markdown(training_markdown, unsafe_allow_html=True)

            # Display the session plans for the Under 8's section
            with st.expander("Session Plans", icon=":material/note_alt:"):
                st.markdown(sessions_markdown, unsafe_allow_html=True)
        elif current_tab == 5:
            # Read the markdown content for the Under 7's section
            summary_markdown = read_markdown_file('content/coaching/minis/under 7s/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/under 7s/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/under 7s/session plans.md')

            # Display the infographic for the Under 7's section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/under 7s/info.png")

            # Display the summary for the Under 7's section
            with st.expander("Summary", icon=":material/format_text_clip:"):
                st.markdown(summary_markdown, unsafe_allow_html=True)

            # Display the training plan for the Under 7's section
            with st.expander("Training Plan", icon=":material/assignment:"):
                st.markdown(training_markdown, unsafe_allow_html=True)

            # Display the session plans for the Under 7's section
            with st.expander("Session Plans", icon=":material/note_alt:"):
                st.markdown(sessions_markdown, unsafe_allow_html=True)
        elif current_tab == 6:
            # Read the markdown content for the Micros section
            summary_markdown = read_markdown_file('content/coaching/minis/micros/summary.md')
            training_markdown = read_markdown_file('content/coaching/minis/micros/training plan.md')
            sessions_markdown = read_markdown_file('content/coaching/minis/micros/session plans.md')

            # Display the infographic for the Micros section
            with st.expander("Infographic", icon=":material/info:"):
                st.image("content/coaching/minis/micros/info.png")

