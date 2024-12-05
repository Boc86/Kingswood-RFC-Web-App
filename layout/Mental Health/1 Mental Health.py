# This script creates a Streamlit app for the Mental Health section of the Kingswood Rugby Club website.
#
# It reads markdown content from files in the 'content/mental health' directory, and displays it in a Streamlit app.
#
# The app has a banner image, and a body section.


# Import the necessary libraries
import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read the markdown content for the body section
body_markdown = read_markdown_file('content/mental health/mental health/body.md')

# Set the banner image for the app
banner = "images/mental health/banner.jpg"

# Display the banner image
st.image(banner)

# Create a container for the body section
with st.container():
    # Display the markdown content for the body section
    st.markdown(body_markdown, unsafe_allow_html=True)
