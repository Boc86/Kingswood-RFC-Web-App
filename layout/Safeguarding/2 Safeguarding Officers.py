# This script creates a Streamlit app for the Safeguarding Officers section of the Kingswood Rugby Club website.
#
# It reads markdown content from files in the 'content/safeguarding/safeguarding officers' directory, and displays it in a Streamlit app.
#
# The app has a banner image, an intro section, and a section with the names of the two Safeguarding Officers.


import streamlit as st
from funcs.read_markdown import read_markdown_file


# Read the markdown content for the intro section
into_markdown = read_markdown_file('content/safeguarding/safeguarding officers/intro.md')

# Set the banner image for the app
banner = "images/safeguarding/banner.png"

# Display the banner image
st.image(banner)

# Add a horizontal divider to separate the title from the content
st.divider()

# Create a container to hold the intro section
with st.container():
    # Display the markdown content for the intro section
    st.markdown(into_markdown, unsafe_allow_html=True)

    # Create two columns, one for each Safeguarding Officer
    left_col, right_col = st.columns(2)

    # Create a subheader for the first Safeguarding Officer
    with left_col:
        st.subheader("Kirsty Lovell")   

    # Create a subheader for the second Safeguarding Officer
    with right_col:
        st.subheader("Gemma Ryan")
