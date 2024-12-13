# This file contains the layout for the Coaching Resources section of the Coaches Handbook

# Import the necessary libraries
import streamlit as st
from forms.resource import resource_form
from funcs.read_markdown import read_markdown_file
from funcs.flip_book import set_flip_book
import supabase
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Initialize Supabase client
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

#conenct to database and run queries
resources = (
    supabase_client
    .table('resources')
    .select('*')
    .order('created_at', desc=True)
    .execute()

)

# Read the markdown content for the intro from the file
intro_markdown = read_markdown_file('content/coaching/resources/intro.md')

# Define a function to show the dialog box to add a resource
@st.dialog("Share a resource")
def show_resource_form():
    ###This function renders a form to submit a resource with a title, link, and description.###
    resource_form()

# Set the title of the page to "Coaching Resources"
st.title("Coaching Resources")

# Display the markdown content on the page, allowing HTML if present
st.markdown(intro_markdown, unsafe_allow_html=True)

with st.expander("Coaches Mail Shot", icon=":material/mail:"):
    set_flip_book('images/coaching/resources/latest mail shot/', "LatestMailShot")

i = 0
with st.expander("Resources", icon=":material/library_books:"):
    # Create a container to hold the resources
    with st.container(height=650, border=True):
        # Loop through each row in the dataframe
        for row in resources.data:
            # Display the title, link, and description of the resource
            st.markdown(f"**Title**: " + resources.data[i]['title'])
            st.markdown(f"**Link**: " + resources.data[i]['link'])
            st.markdown(f"**Description**: " + resources.data[i]['description'])
            st.markdown(f"**Tarhet Audience**: " + resources.data[i]['target_audience'])
            st.markdown(f"**Added by**: " + resources.data[i]['created_by'] + " on " + resources.data[i]['created_at'])
            # Add a horizontal divider to separate the resources
            st.write("---")
            i += 1
        # Add a button to show the dialog box to add a resource
        st.button("Share a resource", on_click=show_resource_form)

