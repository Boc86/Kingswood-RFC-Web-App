# Import the required libraries
import streamlit as st
from funcs.read_markdown import read_markdown_file
from funcs.flip_book import set_flip_book

# Read in the markdown content from a file
intro_markdown = read_markdown_file('content/policies/intro.md')

# Specify the path to the banner image
banner = "images/policies/banner.jpg"
# Display the banner image at the top of the page
st.image(banner)

# Add a horizontal divider to separate the title from the rest of the content
st.divider()

# Create a container to hold the main content
with st.container():
    # Display the markdown content, allowing HTML if present
    st.markdown(intro_markdown, unsafe_allow_html=True)

with st.container():
    with st.expander("Safeguarding", icon=":material/enhanced_encryption:"):
        set_flip_book('images/policies/safeguarding policy/', "safeguarding")
    
    with st.expander("Medical Emergency Action Plan", icon=":material/medical_services:"):
        set_flip_book('images/policies/meap/', "meap")
