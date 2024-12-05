# This script creates a Streamlit app for the Player Info section of the Kingswood Rugby Club website.
#
# It reads markdown content from files in the 'content/player info' directory, and displays it in a Streamlit app.
#
# The app has a banner image, a welcome header, and a body section.

import streamlit as st
from funcs.read_markdown import read_markdown_file


# Read the markdown content for the body section
body_markdown = read_markdown_file('content/player info/welcome letter/body.md')


# Set the banner image for the app
banner = "images/player info/banner.png"


# Display the banner image
st.image(banner)


# Set the welcome header
st.header("Welcome to the Kingswood Rugby Club!")

# Add a horizontal divider
st.divider()


# Create a container with two columns
with st.container():

    # Create two columns, one for the main content and one for the useful links
    left_col, right_col = st.columns(2)


    # Display the markdown content in the left column
    with left_col:
        # Display the markdown content for the body section
        st.markdown(body_markdown, unsafe_allow_html=True)
    
    # Display the useful links in the right column
    with right_col:
        # Add a subheader for the section containing useful links
        st.subheader("Useful Links")
        
        # Link to the How To page
        st.page_link(
            "layout/Home/2 HowTo.py",
            label=None,
            icon=":material/help:",
            help=None,
            disabled=False,
            use_container_width=None
        )
        
        # Link to the Parent Volunteering page
        st.page_link(
            "layout/Parent Info/2 Parent Volunteering.py",
            label=None,
            icon=":material/volunteer_activism:",
            help=None,
            disabled=False,
            use_container_width=None
        )
        
        # Link to the Coaching Team page
        st.page_link(
            "layout/Coaching/2 Coaching Team.py",
            label=None,
            icon=":material/diversity_2:",
            help=None,
            disabled=False,
            use_container_width=None
        )
        
        # Link to the Safeguarding page
        st.page_link(
            "layout/Safeguarding/1 Safeguarding.py",
            label=None,
            icon=":material/enhanced_encryption:",
            help=None,
            disabled=False,
            use_container_width=None
        )
        
        # Link to the Mental Health page
        st.page_link(
            "layout/Mental Health/1 Mental Health.py",
            label=None,
            icon=":material/health_and_safety:",
            help=None,
            disabled=False,
            use_container_width=None
        )
        
        # Link to the Policies page
        st.page_link(
            "layout/Policies/1 Policies.py",
            label=None,
            icon=":material/topic:",
            help=None,
            disabled=False,
            use_container_width=None
        )
