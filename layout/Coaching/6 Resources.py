# This file contains the layout for the Coaching Resources section of the Coaches Handbook

# Import the necessary libraries
import streamlit as st
from streamlit_gsheets import GSheetsConnection as GSC
from forms.resource import resource_form
from funcs.read_markdown import read_markdown_file

# Read the markdown content for the intro from the file
intro_markdown = read_markdown_file('content/coaching/resources/intro.md')

# Connect to the Google Sheets API
conn = st.connection("gsheets", type=GSC)

# Read the data from the Google Sheet
df = conn.read(worksheet=1442126310, ttl=0)

# Define a function to show the dialog box to add a resource
@st.dialog("Share a resource")
def show_resource_form():
    ###This function renders a form to submit a resource with a title, link, and description.###
    resource_form()

# Set the title of the page to "Coaching Resources"
st.title("Coaching Resources")

# Display the markdown content on the page, allowing HTML if present
st.markdown(intro_markdown, unsafe_allow_html=True)

# Create a container to hold the resources
with st.container(height=650, border=True):
    # Loop through each row in the dataframe
    for row in df.itertuples():
        # Display the title, link, and description of the resource
        st.markdown(f"**Title**: {row.resource}")
        st.markdown(f"**Link**: {row.link}")
        st.markdown(f"**Description**: {row.description}")
        # Add a horizontal divider to separate the resources
        st.write("---")

# Add a button to show the dialog box to add a resource
st.button("Share a resource", on_click=show_resource_form)
