import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read the body markdown content from a file
body_markdown = read_markdown_file('content/home/home/body.md')
mission_markdown = read_markdown_file('content/home/home/mission.md')

# Specify the path to the banner image
banner = "images/home/banner.jpg"

# Display the banner image at the top of the page
st.image(banner, use_container_width=True)

# Create a container for the welcome message
with st.container():
    # Display a header with a welcome message
    st.header("👋 Welcome to the Kingswood Rugby Club Volunteers Community!")
    # Display the body markdown content, allowing HTML if present
    st.markdown(body_markdown, unsafe_allow_html=True)

    "---"

# Create another container for useful links
with st.container():
    # Define a layout with two columns
    left_col, right_col = st.columns(2)

    # In the left column, display a subheader and useful links
    with left_col:
        st.subheader("Useful Links")
        # Add page links with icons
        st.page_link("layout/Home/2 HowTo.py", label=None, icon=":material/help:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Parent Info/1 Parent Info.py", label=None, icon=":material/info:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Player Info/1 Player Info.py", label=None, icon=":material/info:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Coaching/2 Coaching Team.py", label=None, icon=":material/diversity_2:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Safeguarding/1 Safeguarding.py", label=None, icon=":material/enhanced_encryption:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Mental Health/1 Mental Health.py", label=None, icon=":material/health_and_safety:", help=None, disabled=False, use_container_width=None)
        st.page_link("layout/Policies/1 Policies.py", label=None, icon=":material/topic:", help=None, disabled=False, use_container_width=None)  
    
    # In the right column, leave it empty for future use
    with right_col:
        st.subheader("👑Mission Statement👑")
        st.markdown(mission_markdown, unsafe_allow_html=True)
