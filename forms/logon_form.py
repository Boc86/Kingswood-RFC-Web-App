import streamlit as st
import supabase
import os
from dotenv import load_dotenv
import hashlib
import re

# Load environment variables
load_dotenv()

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Initialize Supabase client
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

def validate_username(username):
    """Check for duplicate username"""
    response = supabase_client.table('logons').select('username').eq('username', username).execute()

    res = " " in username

    try:
        if res:
            st.error("Username cannot contain spaces")
            return False

        if not str(response.count) == "None":
            # Check if annual subs have been paid
            st.error("User name already in use, please choose a different one")
            return False
    except Exception as e:
        st.error(f"Login error: {e}")

    return True

def hash_password(password):
    """Simple password hashing function."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    """
    Validate email format with more comprehensive regex.
    
    Checks for:
    - One or more characters before the @
    - A domain name after @
    - A top-level domain of 2-4 characters
    - Allows for valid special characters in local part
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
    
    # Additional specific checks
    if not re.match(email_regex, email):
        return False
    
    # Ensure no consecutive dots in local part
    if '..' in email.split('@')[0]:
        return False
    
    # Ensure domain has at least one dot
    domain = email.split('@')[1]
    if '.' not in domain:
        return False
    
    return True

def validate_rfu_id(rfu_id):
    """
    Validate RFU ID:
    """
    
    try:
        # Fetch user from Supabase
        response = supabase_client.table('members').select('*').eq('rfu_id', rfu_id).execute()
        print(response)
        rfu_regex = r'^[0-9]+$'
        if not rfu_id:
            st.error("RFU ID cannot be blank")
            return False
        
        if not re.match(rfu_regex, rfu_id):
            st.error("RFU ID must be numeric only")
            return False
        
        if not response.data:
            st.error("RFU ID does not exist")
            return False
        
    except Exception as e:
        st.error(f"Login error: {e}")
        return False
    
    return True

def check_login(username, password):
    """Check user credentials against Supabase."""
    hashed_password = hash_password(password)
    
    try:
        # Fetch user from Supabase
        response = supabase_client.table('logons').select('*').eq('username', username).execute()
        
        if response.data and len(response.data) > 0:
            # Compare hashed passwords
            stored_user = response.data[0]
            return stored_user['password'] == hashed_password
    except Exception as e:
        st.error(f"Login error: {e}")
        return False

def register_user(username, email, rfu_id, password):
    """Register a new user in Supabase."""
    try:
        
        # Check if info already exists
        existing_email = supabase_client.table('logons').select('*').eq('email', email).execute()
        existing_user_name = supabase_client.table('logons').select('*').eq('username', username).execute()
        
        if existing_user_name.data and len(existing_user_name.data) > 0:
            st.error("Username already registered")
            return False
        elif existing_email.data and len(existing_email.data) > 0:
            st.error("Email already in use")
            return False

        
        # Hash the password
        hashed_password = hash_password(password)
        
        # Insert new user
        new_user = {
            'username': username, 
            'email': email,
            'rfu_id': rfu_id,
            'password': hashed_password
        }
        
        supabase_client.table('logons').insert(new_user).execute()
        return True
    
    except Exception as e:
        st.error(f"Registration error: {e}")
        return False

def update_password(fgt_rfu_id, fgt_password):
    
    fgt_hashed_password = hash_password(fgt_password)

    try:
        supabase_client.table('logons').update({'password': fgt_hashed_password}).eq('rfu_id', fgt_rfu_id).execute()
        return True

    except Exception as e:
        st.error(f"Registration error: {e}")
        return False

def login_form():

    with st.form(key="Feedback"):

        """Streamlit login page."""
        st.title("👑 KRFC Knowledge Login / Register")
        st.text("Please note that user names are case sensitive.")
        
        # Create tabs
        tab1, tab2, tab3 = st.tabs(["Login", "Register", "Forgot Password"])
        
        with tab1:
            st.header("Login")
            login_username = st.text_input("Username", key="login_username")
            login_password = st.text_input("Password", type="password", key="login_password")
            login_button: bool = st.form_submit_button(label="Login")
            
            if login_button:
                if check_login(login_username, login_password):
                    # Store login state
                    st.session_state['logged_in'] = True
                    st.session_state['username'] = login_username


                    get_rfu_id = supabase_client.table('logons').select('rfu_id').eq('username', login_username).execute()
                    reg_rfu_id = str(get_rfu_id.data[0]['rfu_id'])  
                    st.session_state['rfu_id'] = reg_rfu_id

                    get_user_name = supabase_client.table('members').select('first_name').eq('rfu_id', reg_rfu_id).execute()
                    st.session_state['first_name'] = str(get_user_name.data[0]['first_name'])
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        with tab2:
            st.header("Register")
            # Registration form with added fields
            reg_username = st.text_input("Choose a Username", key="reg_username")
            reg_email = st.text_input("Email Address", key="reg_email")
            reg_rfu_id = st.text_input("RFU ID, you can obtain your RFU IF from the RGU GMS Dashboard", key="reg_rfu_id")
            reg_password = st.text_input("Create a Password", type="password", key="reg_password")
            confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
            register_button: bool = st.form_submit_button(label="Register")
            
            if register_button:
                # Comprehensive validation
                validation_errors = []
                
                # Username validation
                if len(reg_username) < 3:
                    validation_errors.append("Username must be at least 3 characters long")
                
                if not validate_username(reg_username):
                    validation_errors.append("Username already exists please select a different one")
                
                # Email validation
                if not validate_email(reg_email):
                    validation_errors.append("Invalid email address format")
                
                # RFU ID validation
                if not validate_rfu_id(reg_rfu_id):
                    validation_errors.append("You are not affiliated with Kingswood RFC on the RFU GMS system. This could be becasue you haven't paid your annual subscription. If you have not paid your annual subs please do so on the RFU GMS website. If you believe you have already paid your subs please contact Tom Lovell.")
                
                # Password validations
                if len(reg_password) < 6:
                    validation_errors.append("Password must be at least 6 characters long")
                
                if reg_password != confirm_password:
                    validation_errors.append("Passwords do not match")

                # Display or proceed with registration
                if validation_errors:
                    for error in validation_errors:
                        st.error(error)
                else:
                    # Attempt registration
                    if register_user(reg_username, reg_email, reg_rfu_id, reg_password):
                        st.success("Registration successful! You can now log in.")
        
        with tab3:
            st.header("Forgot Password")
            # Forgot password fields
            fgt_username = st.text_input("The user name you registered with", key="fgt_username")
            fgt_email = st.text_input("The email address you registered with", key="fgt_email")
            fgt_rfu_id = st.text_input(" The RFU ID you resgitered with, you can obtain your RFU IF from the RGU GMS Dashboard", key="fgt_rfu_id")
            new_password =""
            new_confirm_password = ""

            fgt_button: bool = st.form_submit_button(label="Check Details")
            st.text("Please confirm your details before clicking Change Password. Once your details are veified two new password fields will become visible")

            if fgt_button:
                # Comprehensive validation
                validation_errors = []

                if not validate_username(fgt_username):
                    validation_errors.append("Username not recognised")
                
                # Email validation
                if not validate_email(fgt_email):
                    validation_errors.append("Invalid email address format")
                
                # RFU ID validation
                if not validate_rfu_id(fgt_rfu_id):
                    validation_errors.append("RFU ID not recognised.")
                
                #Display or proceed with password reset
                if validation_errors:
                    for error in validation_errors:
                        st.error(error)
                else:
                    # Attempt registration
                    if len(validation_errors) == 0:
                        st.success("Please set a new password.")
                        st.text_input("New Password", type="password", key="fgt_new_password")
                        st.text_input("Confirm Password", type="password", key="new_confirm_password")                    
            
            change_button: bool = st.form_submit_button(label= "Change Password")

            if change_button:
                new_password = st.session_state['fgt_new_password']
                new_confirm_password = st.session_state['new_confirm_password']
                if new_password != new_confirm_password:
                    st.error("Passwords do not match")
                    return
                else:
                    if update_password(fgt_rfu_id, new_password):
                        st.success("Password reset successful! You can now log in.")
                    else:
                        st.error("Password reset failed. Please try again.")
                                
