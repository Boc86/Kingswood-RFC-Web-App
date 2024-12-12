import streamlit as st
from funcs.read_markdown import read_markdown_file
import supabase
import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Initialize Supabase client
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

# Read the markdown content for the intro section
intro_markdown = read_markdown_file('content/home/key personnel/intro.md')

# Set the banner image for the app
banner = "images/home/banner.jpg"

#conenct to database and run queries
committee = supabase_client.table('members').select('*').eq('key_person', "y").order('last_name', desc=True).execute()
safe = supabase_client.table('members').select('*').eq('type', "safeguarding").order('last_name', desc=False).execute()
events = supabase_client.table('members').select('*').eq('type', "events").order('last_name', desc=False).execute()

# Display the banner image
st.image(banner)

with st.container():
    # Display the markdown content for the intro section
    st.markdown(intro_markdown, unsafe_allow_html=True)

with st.expander("Committee Members", icon=":material/partner_exchange:"):
    i = 0
    for rows in committee.data:
        st.subheader(str(committee.data[i]['first_name']) + " " + str(committee.data[i]['last_name']))
        st.write(str(committee.data[i]['title']))
        st.write("---")
        i += 1

with st.expander("Safeguarding Team", icon=":material/escalator_warning:"):
    i = 0
    for rows in safe.data:
        st.subheader(str(safe.data[i]['first_name']) + " " + str(safe.data[i]['last_name']))
        st.write(str(safe.data[i]['title']))
        st.write("---")
        i += 1

with st.expander("Events Committee", icon=":material/celebration:"):
    i = 0
    for rows in events.data:
        st.subheader(str(events.data[i]['first_name']) + " " + str(events.data[i]['last_name']))
        st.write(str(events.data[i]['title']))
        st.write("---")
        i += 1