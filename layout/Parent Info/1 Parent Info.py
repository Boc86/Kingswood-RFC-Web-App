# This script creates a Streamlit app for the Parent Info section of the Kingswood Rugby Club web site.
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
body_markdown = read_markdown_file('content/parent info/welcome letter/body.md')

# Display the banner image at the top of the page
banner = "images/parent info/banner.jpg"
st.image(banner)

# Set the title of the page
st.header("Welcome to the Kingswood Rugby Club!")

# Add a horizontal divider to separate the title from the rest of the content
st.divider()

# Create a container to hold the main content and the useful links
with st.container():

    # Create two columns, one for the main content and one for the useful links
    lef_col, right_col = st.columns(2)

    # Display the markdown content in the left column
    with lef_col:
        st.markdown(body_markdown, unsafe_allow_html=True)
    
    # Display the useful links in the right column
    with right_col:
        st.subheader("Useful Links")

        # Create clickable links to the other pages in the web site
        st.page_link("layout/Home/2 HowTo.py", label=None, icon=":material/help:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Parent Info/2 Parent Volunteering.py", label=None, icon=":material/volunteer_activism:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Coaching/2 Coaching Team.py", label=None, icon=":material/diversity_2:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Safeguarding/1 Safeguarding.py", label=None, icon=":material/enhanced_encryption:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Mental Health/1 Mental Health.py", label=None, icon=":material/health_and_safety:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Policies/1 Policies.py", label=None, icon=":material/topic:", help=None, disabled=False, use_container_width=None)  
