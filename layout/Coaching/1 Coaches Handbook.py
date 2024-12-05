import streamlit as st
from funcs.read_markdown import read_markdown_file

# Read the introductory markdown content for the Coaches Handbook
body_markdown = read_markdown_file('content/coaching/coaches handbook/intro.md')

# Display the banner image for the coaching section
st.image("images/coaching/banner.png")

# Set the title of the page to "Coaches Handbook"
st.title("Coaches Handbook")

# Display the markdown content on the page, allowing HTML if present
st.markdown(body_markdown, unsafe_allow_html=True)

# Create a container to hold a horizontal divider and useful links
with st.container():
    # Add a horizontal divider
    st.write("---")

    # Add a subheader for the section containing useful links
    st.subheader("Useful Links")
    
    # Link to the Coaching Team section
    st.page_link(
        "layout/Coaching/2 Coaching Team.py",
        label=None,
        icon=":material/diversity_2:",
        help=None,
        disabled=False,
        use_container_width=None
    )
    
    # Link to the Juniors section
    st.page_link(
        "layout/Coaching/3 Juniors.py",
        label=None,
        icon=":material/man:",
        help=None,
        disabled=False,
        use_container_width=None
    )
    
    # Link to the Athenas section
    st.page_link(
        "layout/Coaching/4 Athenas.py",
        label=None,
        icon=":material/woman:",
        help=None,
        disabled=False,
        use_container_width=None
    )
    
    # Link to the Minis section
    st.page_link(
        "layout/Coaching/5 Minis.py",
        label=None,
        icon=":material/boy:",
        help=None,
        disabled=False,
        use_container_width=None
    )
    
    # Link to the Resources section
    st.page_link(
        "layout/Coaching/6 Resources.py",
        label=None,
        icon=":material/share:",
        help=None,
        disabled=False,
        use_container_width=None
    )
