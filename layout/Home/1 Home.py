import streamlit as st

banner = "images/Home/banner.jpg"

with st.container():

    st.image(banner)
    st.header("👋 Welcome to the Kingswood Rugby Club Volunteers Community!")
    st.markdown("""
        We are thrilled to welcome you to our dynamic and 
        vibrant community dedicated to supporting the invaluable efforts of our volunteers. Whether you're a seasoned 
        member of our club or just stepping into the world of rugby volunteering, this app is your gateway to all the 
        essential resources and information you need to excel in your role. Within this hub, you'll find a treasure 
        trove of resources tailored to empower you in your volunteer journey. From important contacts to comprehensive 
        club policies and procedures, we've curated a one-stop destination to streamline your experience and ensure 
        you have everything at your fingertips to thrive in your role. As a volunteer, you play a pivotal role in shaping 
        the Kingswood Rugby Club experience for our players, supporters, and community. Your dedication and passion are 
        the backbone of our club, and we are deeply grateful for your commitment to our shared vision. We encourage you 
        to explore this community, engage with fellow volunteers, and take advantage of the wealth of knowledge and support 
        available to you. Together, we will continue to uphold the spirit of teamwork, sportsmanship, and camaraderie that 
        defines Kingswood Rugby Club. Thank you for being a part of our Volunteers Community. We look forward to embarking 
        on this exciting journey together and creating lasting memories both on and off the field.
        """
    )

with st.container():
    st.write("---")

    st.subheader("Usefull Links 🔗")
    st.page_link("layout/Home/2 HowTo.py")
    st.page_link("layout/Parent Info/1 Parent Info.py")
    st.page_link("layout/Player Info/1 Player Info.py")
    st.page_link("layout/Coaching/2 Coaching Team.py")
    st.page_link("layout/Safeguarding/1 Safeguarding.py")
    st.page_link("layout/Mental Health/1 Mental Health.py")
    st.page_link("layout/Policies/1 Policies.py")
        