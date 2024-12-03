import re
import streamlit as st
import requests


WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZmMDYzNzA0MzY1MjZiNTUzNTUxMzEi_pc"

def is_valid_email(email):
     email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
     return re.match(email_pattern, email) is not None

def feddback_form():
    with st.form(key="Feedback"):
        name= st.text_input("Name")
        email= st.text_input("Email")
        feedback= st.text_area("Feedback")
        submit_button = st.form_submit_button(label="Submit")
    
    if submit_button:
        if not WEBHOOK_URL:
            st.error(
                "Email service is not set up. Please try again later."
                )
            st.stop
    
        if not name:
            st.error("Please enter your name.")
            st.stop

        if not is_valid_email(email):
            st.error("Please enter a valid email address.")
            st.stop

        if not feedback:
            st.error("Please enter your feedback.")
            st.stop

        data = {"email": email, "name": name, "feedback": feedback}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Thanks for your feedback! We will get back to you soon.")
        else:
            st.error("There was an error sending your message. Please try again later.")