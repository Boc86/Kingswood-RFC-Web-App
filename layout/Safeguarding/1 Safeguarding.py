# Import the required libraries
import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read in the markdown content from a file
body_markdown = read_markdown_file('content/safeguarding/safeguarding/body.md')

# Specify the path to the banner image
banner = "images/safeguarding/banner.png"
# Display the banner image at the top of the page
st.image(banner)

# Add a horizontal divider to separate the title from the rest of the content
st.divider()

# Create a container to hold the main content
with st.container():
    # Display the markdown content, allowing HTML if present
    st.markdown(body_markdown, unsafe_allow_html=True)

