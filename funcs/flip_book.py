import streamlit as st
from PIL import Image
import os

def set_flip_book(image_paths, unique_key):
    # Calculate total pages
    total_pages = len([entry for entry in os.listdir(image_paths) if os.path.isfile(os.path.join(image_paths, entry))])
    
    # Initialize page number if not already set
    if f'page_number_{unique_key}' not in st.session_state:
        st.session_state[f'page_number_{unique_key}'] = 1

    # Main display column
    col1, col2 = st.columns(2)

    with col1:
        # Navigation buttons with unique keys
        col_prev, col_next = st.columns(2)
        
        with col_prev:
            prev_button = st.button('Previous Page', 
                disabled=st.session_state[f'page_number_{unique_key}'] < 1,
                key=f'prev_page_btn_{unique_key}'
            )
        
        with col_next:
            next_button = st.button('Next Page', 
                disabled=st.session_state[f'page_number_{unique_key}'] >= total_pages,
                key=f'next_page_btn_{unique_key}'
            )
        
        # Handle page navigation
        if prev_button and st.session_state[f'page_number_{unique_key}'] > 1:
            st.session_state[f'page_number_{unique_key}'] -= 1
        elif next_button and st.session_state[f'page_number_{unique_key}'] < total_pages:
            st.session_state[f'page_number_{unique_key}'] += 1

        # Load and display selected page
        try:
            image_file = os.path.join(image_paths, f"page_{st.session_state[f'page_number_{unique_key}']}.jpg")
            selected_page = Image.open(image_file)
            st.image(selected_page, width=700)
        except Exception as img_error:
            st.error(f"Error loading image: {img_error}")
        
        # Display current page number
        st.write(f'Page {st.session_state[f"page_number_{unique_key}"]} of {total_pages}')
    
    with col2:
        st.empty()