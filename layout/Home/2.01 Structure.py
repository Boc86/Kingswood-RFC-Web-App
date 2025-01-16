import streamlit as st
import pandas as pd
from funcs.read_markdown import read_markdown_file

# Read the markdown content for the intro section
intro_markdown = read_markdown_file('content/home/structure/intro.md')
body_markdown = read_markdown_file('content/home/structure/body.md')

# Set the banner image for the app
banner = "images/home/banner.jpg"
structure = "content/home/structure/structure.drawio.svg"

# Display the banner image
st.image(banner)


# Create a container for the intro section
with st.container():
    # Display the markdown content for the intro section
    st.markdown(intro_markdown, unsafe_allow_html=True)
    st.image(structure)

    