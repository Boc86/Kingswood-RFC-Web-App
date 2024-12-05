# This script creates a Streamlit app for the Parent Volunteering section of the Kingswood Rugby Club web site.
#
# The script reads in a markdown file and displays it in a Streamlit app, along with a banner image and a set of useful links.
#
# The useful links point to other pages in the web site, and are displayed in a separate column to the right of the main content.
#
# The script also defines a Streamlit page link function, which is used to create clickable links to the other pages in the web site.

# Import the required libraries
import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read in the markdown content from a file
body_markdown = read_markdown_file('content/parent info/volunteering/body.md')

# Display the banner image at the top of the page
banner = "images/parent info/banner.jpg"
st.image(banner)

# Set the title of the page
st.header("Volunteering")

# Add a horizontal divider to separate the title from the rest of the content
st.divider()

# Create a container to hold the main content and the useful links
with st.container():
    # Display the markdown content on the page, allowing HTML if present
    st.markdown(body_markdown, unsafe_allow_html=True)

