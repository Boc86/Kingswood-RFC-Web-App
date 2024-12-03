import streamlit as st

banner = "images/home/banner.jpg"
st.image(banner)

with st.container():
    st.markdown(open('content/home/how to/intro.txt').readlines())

    tab1, tab2, tab3, tab4 = st.tabs(["Navigation", "Contribute", "Discussion", "Feedback"])

    tab1.markdown(open('content/home/how to/tab1.txt').readlines())
    
    tab2.markdown(open('content/home/how to/tab2.txt').readlines())
    
    tab3.markdown(open('content/home/how to/tab3.txt').readlines())
    
    with tab4: 
        st.markdown(open('content/home/how to/tab4.txt').readlines())
        st.write("###")
        with st.form(key="Feedback"):
            name= st.text_input("Name")
            email= st.text_input("Email")
            feedback= st.text_area("Feedback")
            submit_button = st.form_submit_button(label="Submit")