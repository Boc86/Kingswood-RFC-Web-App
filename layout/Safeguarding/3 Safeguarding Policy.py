# This script creates a Streamlit app for the Safeguarding Policy page of the Kingswood Rugby Club web site.
#
# It reads markdown content from a file in the 'content/safeguarding' directory, and displays it in a Streamlit app.
#
# The app has a banner image at the top, followed by a horizontal divider, and then the markdown content below that.


import streamlit as st
from funcs.read_markdown import read_markdown_file
from funcs.flip_book import set_flip_book

# Read the markdown content for the page from a file
body_markdown = read_markdown_file('content/safeguarding/safeguarding policy/body.md')

# Set the path to the banner image
banner = "images/safeguarding/banner.png"

# Display the banner image at the top of the page
st.image(banner)

# Add a horizontal divider to separate the banner from the rest of the content
st.divider()

# Create a container to hold the markdown content
with st.container():
    # Display the markdown content in the container
    set_flip_book('images/policies/safeguarding policy/', "safeguarding")
