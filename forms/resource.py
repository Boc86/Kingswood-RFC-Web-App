import streamlit as st
import requests
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

def add_resource(title, link, description, target_audience):
    """Add resource in Supabase."""
    try:
        # Insert resource
        new_resource = {
            'title': title, 
            'link': link, 
            'description': description, 
            'target_audience': target_audience, 
            'created_by': created_by, 
            'rfu_id': user
        }
        
        response = (
            supabase_client.table('resources')
            .insert(new_resource)
            .execute()
        )
        return True
    
    except Exception as e:
        st.error(f"Error adding resource: Please contact your admin.")
        return False

# Pull back RFU ID and Name
user = st.session_state['rfu_id']
created_by = supabase_client.table('members').select('*').eq('rfu_id', user).execute().data[0]['first_name'] + " " + supabase_client.table('members').select('*').eq('rfu_id', user).execute().data[0]['last_name']

def resource_form():
    """Renders a form to submit a resource with a name, link, and description."""
    with st.form(key="Add a resource"):
        # Input field for the resource name
        input_resource = st.text_input("Resource")
        # Input field for the resource link
        input_link = st.text_input("Link")
        # Input field for the resource description
        input_description = st.text_input("Description")
        # Input field for the resource description
        input_target = st.text_input("Target Audience, i.e. All Coaches")
        # Submit button for the form
        submit_button = st.form_submit_button(label="Submit")
    
    # Check if the submit button was clicked
    if submit_button:
    
        # Ensure the resource name is provided
        if not input_resource:
            st.error("Please enter a name for your resource.")
            st.stop

        # Ensure the resource link is provided
        if not input_link:
            st.error("Please enter a website link.")
            st.stop
        
        # Ensure the resource description is provided
        if not input_description:
            st.error("Please enter a description of the resource.")
            st.stop
        
        # Ensure the resource description is provided
        if not input_target:
            st.error("Please enter a target audience for the resource.")
            st.stop

        # Write date to DB
        

        # Check the response status and display appropriate message
        if add_resource(input_resource, input_link, input_description, input_target):
            st.success("Thanks for sharing a resource you may no close this window")
            st.rerun
