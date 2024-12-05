# This file contains the layout for the message board section of the Coaches Handbook

import streamlit as st
from streamlit_gsheets import GSheetsConnection as GSC
from forms.message import message_form
from funcs.read_markdown import read_markdown_file


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
with st.container(height=650, border=True):
    ###    This container will hold the message board content. The message board will be displayed in a scrollable area, and each message will be separated by a horizontal line.     ###
    
    # Iterate over each row in the dataframe containing the message board data
    for row in df.itertuples():
        # Display the name of the person who posted the message
        st.markdown(f"**Posted by**: {row.name} @ {row.date}")
        
        # Display the message
        st.markdown(f"**Message**: {row.message}")
        
        # Add a horizontal line to separate each message
        st.write("---")



# Add a button which will call the show_message_form function when clicked
st.button("Submit a message", on_click=show_message_form)
