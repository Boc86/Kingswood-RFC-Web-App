import streamlit as st
from PIL import Image
import os


def set_flip_book(image_paths):

    total_pages = len([entry for entry in os.listdir(image_paths) if os.path.isfile(os.path.join(image_paths, entry))])
    
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1

    # Main display column
    col1, col2 = st.columns(2)

    with col1:
        # Navigation buttons
        col_prev, col_next, col_next = st.columns([1,2,1])
        
        with col_prev:
            prev_button = st.button('Previous Page', 
                disabled=st.session_state.page_number == 1
            )
        
        with col_next:
            next_button = st.button('Next Page', 
                disabled=st.session_state.page_number >= total_pages
            )
        
        # Handle page navigation
        if prev_button and st.session_state.page_number > 1:
            st.session_state.page_number -= 1
        elif next_button and st.session_state.page_number < total_pages:
            st.session_state.page_number += 1
        
        # Load and display selected page
        try:
            image_file = str(image_paths) + "/" + "page_" + str(st.session_state.page_number) + ".jpg"
            selected_page = Image.open(
                image_file
            )
            print(selected_page)
            # Replace use_c_width with width parameter
            st.image(selected_page, width=700)
        except Exception as img_error:
            print(selected_page)
            st.error(f"Error loading image: {img_error}")
            st.error(f"Could not load page image: {img_error}")
        
        # Display current page number
        st.write(f'Page {st.session_state.page_number} of {total_pages}')
    
    with col2:
        st.empty()