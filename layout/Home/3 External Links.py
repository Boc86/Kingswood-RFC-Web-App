# This script creates a Streamlit app for the External Links section of the Kingswood Rugby Club website.
#
# It reads markdown content from files in the 'content/home/external links' directory, and displays it in a Streamlit app.
#
# The app has a banner image, an intro section, and a body section.

import streamlit as st
from funcs.read_markdown import read_markdown_file


# Read the markdown content for the intro section
intro_markdown = read_markdown_file('content/home/external links/intro.md')


# Read the markdown content for the body section
body_markdown = read_markdown_file('content/home/external links/body.md')


# Set the banner image for the app
banner = "images/home/banner.jpg"


# Display the banner image
st.image(banner)


# Set the title of the page
st.title("External Links")


# Create a container for the intro section
with st.container():

    # Display the markdown content for the intro section
    st.markdown(intro_markdown, unsafe_allow_html=True)


# Create a container for the body section
with st.container():

    # Display the markdown content for the body section
    st.markdown(body_markdown, unsafe_allow_html=True)
