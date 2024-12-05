# This script creates a Streamlit app for the How To section of the Kingswood Rugby Club website.
#
# It reads markdown content from files in the 'content/home/how to' directory, and displays it in a Streamlit app.
#
# The app has a banner image, an intro section, and three tabs for Navigation, Contribute and Discussion.

import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read the markdown content for the intro section
intro_markdown = read_markdown_file('content/home/how to/intro.md')

# Read the markdown content for the three tabs
tab1_markdown = read_markdown_file('content/home/how to/tab1.md')
tab2_markdown = read_markdown_file('content/home/how to/tab2.md')
tab3_markdown = read_markdown_file('content/home/how to/tab3.md')

# Set the banner image for the app
banner = "images/home/banner.jpg"

# Display the banner image
st.image(banner)

# Create a container for the intro section
with st.container():
    # Display the markdown content for the intro section
    st.markdown(intro_markdown, unsafe_allow_html=True)

# Create a tabs container with three tabs
tab1, tab2, tab3 = st.tabs(["Navigation", "Contribute", "Coaches Discussion"])

# Create a container for the first tab
with tab1:
    # Display the markdown content for the first tab
    st.markdown(tab1_markdown, unsafe_allow_html=True)
    
# Create a container for the second tab
with tab2:
    # Display the markdown content for the second tab
    st.markdown(tab2_markdown, unsafe_allow_html=True)
    
# Create a container for the third tab
with tab3:
    # Display the markdown content for the third tab
    st.markdown(tab3_markdown, unsafe_allow_html=True)
