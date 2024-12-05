import streamlit as st
import requests


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZmMDYzNzA0MzA1MjY1NTUzMDUxMzIi_pc"

def message_form():
    with st.form(key="Feedback"):
        name= st.text_input("Name")
        message= st.text_area("Message")
        submit_button = st.form_submit_button(label="Submit")
    
    if submit_button:
        if not WEBHOOK_URL:
            st.error(
                "Database service is not set up. Please try again later."
                )
            st.stop
    
        if not name:
            st.error("Please enter your name.")
            st.stop

        if not message:
            st.error("Please enter your message.")
            st.stop

        data = {"name": name, "feedback": message}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Thanks for contributing to the discussion. Close this window and press R to refresh the chat board")
        else:
            st.error("There was an error sending your message. Please please submit feedback")