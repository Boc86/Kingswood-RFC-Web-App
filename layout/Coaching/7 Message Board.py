# This file contains the layout for the message board section of the Coaches Handbook

import streamlit as st
from streamlit_gsheets import GSheetsConnection as GSC
from forms.message import message_form
from funcs.read_markdown import read_markdown_file
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
messages = (
    supabase_client
    .table('chat')
    .select('*')
    .order('created_at', desc=True)
    .execute()

)

# Read the introductory markdown content for the Coaches Handbook
intro_markdown = read_markdown_file('content/coaching/message board/intro.md')


# Connect to the Google sheet which contains the message board data
conn = st.connection("gsheets", type=GSC)


# Read the data from the Google sheet
df = conn.read(worksheet=0, ttl=0)


# Define a function which will be called when the user clicks the "Submit a message" button
@st.dialog("Submit a message")
def show_message_form():
    ###This function will be called when the user wants to submit a message to the message board###
    message_form()


# Set the title of the page to "Message Board"
st.title("Message Board")


# Display the markdown content on the page, allowing HTML if present
st.markdown(intro_markdown, unsafe_allow_html=True)

# Create a container to hold the message board
i = 0
with st.container(height=650, border=True):
    # Loop through each row in the dataframe
    for row in messages.data:
        # Display the title, link, and description of the messages
        st.markdown(f"**Title**: " + messages.data[i]['title'])
        st.markdown(f"**Added by**: " + messages.data[i]['created_by'] + " on " + messages.data[i]['created_at'])
        st.markdown(f"**Message**: " + messages.data[i]['message'])
        
        # Add a horizontal divider to separate the messages
        st.write("---")
        i += 1


# Add a button which will call the show_message_form function when clicked
st.button("Submit a message", on_click=show_message_form)
