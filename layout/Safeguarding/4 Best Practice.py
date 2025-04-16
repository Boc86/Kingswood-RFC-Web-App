import streamlit as st
from funcs.read_markdown import read_markdown_file
from funcs.flip_book import set_flip_book

# Read the markdown content for the page from a file
body_markdown = read_markdown_file('content/safeguarding/best practice/body.md')

# Set the path to the banner image
banner = "images/safeguarding/banner.png"

# Display the banner image at the top of the page
st.image(banner)

# Add a horizontal divider to separate the banner from the rest of the content
st.divider()
st.markdown(body_markdown, unsafe_allow_html=True)

# Create a container to hold the markdown content
with st.container():
    # Display the markdown content in the container
    set_flip_book('images/safeguarding/best practice/', "best_practice")