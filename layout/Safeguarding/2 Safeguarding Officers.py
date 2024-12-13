# This script creates a Streamlit app for the Safeguarding Officers section of the Kingswood Rugby Club website.
#
# It reads markdown content from files in the 'content/safeguarding/safeguarding officers' directory, and displays it in a Streamlit app.
#
# The app has a banner image, an intro section, and a section with the names of the two Safeguarding Officers.


import streamlit as st
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
safe = supabase_client.table('members').select('*').eq('type', "safeguarding").order('last_name', desc=False).execute()

# Read the markdown content for the intro section
into_markdown = read_markdown_file('content/safeguarding/safeguarding officers/intro.md')

# Set the banner image for the app
banner = "images/safeguarding/banner.png"

# Display the banner image
st.image(banner)

# Add a horizontal divider to separate the title from the content
st.divider()

# Create a container to hold the intro section
with st.container():
    # Display the markdown content for the intro section
    st.markdown(into_markdown, unsafe_allow_html=True)

# Add each person fron the safeguarding category in the database
i = 0
for rows in safe.data:
    st.subheader(str(safe.data[i]['first_name']) + " " + str(safe.data[i]['last_name']))
    st.write(str(safe.data[i]['title']))
    st.write("---")
    i += 1   

