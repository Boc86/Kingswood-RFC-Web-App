import streamlit as st
import requests


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZmMDYzNzA0MzI1MjZiNTUzMzUxMzIi_pc"

def resource_form():
    with st.form(key="Add a resource"):
        resource= st.text_input("Resource")
        link= st.text_input("Link")
        description= st.text_input("Description")
        submit_button = st.form_submit_button(label="Submit")
    
    if submit_button:
        if not WEBHOOK_URL:
            st.error(
                "Database service is not set up. Please try again later."
                )
            st.stop
    
        if not resource:
            st.error("Please enter a name for your resource.")
            st.stop

        if not link:
            st.error("Please enter a website link.")
            st.stop
        
        if not description:
            st.error("Please enter a description of the resource.")
            st.stop

        data = {"resource": resource, "link": link, "description": description}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Thanks for sharing a resource. Close this window and press R to refresh the chat board")
        else:
            st.error("There was an error sending your message. Please try again later.")