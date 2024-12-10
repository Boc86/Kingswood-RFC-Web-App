# This is the main application file that contains the layout and configuration of the application
import streamlit as st
from PIL import Image
from forms.feedback import feddback_form
from forms.logon_form import login_form

# Application Config
st.set_page_config(
    page_title="KRFC Volunteers Community",
    page_icon="",
    layout="wide"
)

@st.dialog("Login")
def show_login_form() -> None:
    # This function is used to show the login form within a dialog box###
    login_form()

@st.dialog("Send Feedback")
def show_feedback_form() -> None:
    # This function is used to show the feedback form within a dialog box###
    feddback_form()

def main_app():
    """Main application content after login."""

    icon = Image.open('images/logo.png')

    st.title(f"Hi, {st.session_state['username']}!")

    # Navigation Bar
    st.logo(
        image=Image.open('images/logo.png'),
        link="https://www.kingswoodrfc.co.uk",
        size="large",
        icon_image=Image.open('images/icon.png')
    )

    # Pages
    # Home 
    home = st.Page(
        "layout/Home/1 Home.py", title="Home", icon=":material/home:", default= True
    )

    how_to = st.Page(
        "layout/Home/2 HowTo.py", title="How to use the Kingswood RFC Volunteer Community Web App", icon=":material/help:"
    )

    external_links = st.Page(
        "layout/Home/3 External Links.py", title="External Links", icon=":material/captive_portal:"
    )

    club_shop = st.Page(
        "layout/Home/2.1 Club Shop.py", title="Club Shop", icon=":material/shopping_cart:"
    )

    # Parent Info
    parent_info = st.Page(
        "layout/Parent Info/1 Parent Info.py", title="Welcome Letter", icon=":material/info:"
    )

    parent_volunteering = st.Page(
        "layout/Parent Info/2 Parent Volunteering.py", title="Volunteering", icon=":material/volunteer_activism:"
    )

    parent_age_groups = st.Page(
        "layout/Parent Info/3 Parent Age Groups.py", title="Age Groups", icon=":material/pin:"
    )

    # Player Info
    player_info = st.Page(
        "layout/Player Info/1 Player Info.py", title="Player Info", icon=":material/info:"
    )

    # Policies
    policies = st.Page(
        "layout/Policies/1 Policies.py", title="Policies", icon=":material/topic:"
    )

    # Safeguarding
    safeguarding = st.Page(
        "layout/Safeguarding/1 Safeguarding.py", title="Safeguarding", icon=":material/enhanced_encryption:"
    )

    safeguarding_officers = st.Page(
        "layout/Safeguarding/2 Safeguarding Officers.py", title="Safeguarding Officers", icon=":material/group:"
    )

    safeguarding_ploicy = st.Page(
        "layout/Safeguarding/3 Safeguarding Policy.py", title="Safeguarding Policy", icon=":material/description:"
    )

    # Coaching
    coaches_handbook = st.Page(
        "layout/Coaching/1 Coaches Handbook.py", title="Coaches Handbook", icon=":material/hub:"
    )
    coaching_team = st.Page(
        "layout/Coaching/2 Coaching Team.py", title="Coaching Team", icon=":material/diversity_2:"
    )

    coaching_juniors = st.Page(
        "layout/Coaching/3 Juniors.py", title="Juniors", icon=":material/man:"
    )

    coaching_athenas = st.Page(
        "layout/Coaching/4 Athenas.py", title="Athenas", icon=":material/woman:"
    )

    coaching_minis = st.Page(
        "layout/Coaching/5 Minis.py", title="Minis", icon=":material/boy:"
    )

    coaching_resources = st.Page(
        "layout/Coaching/6 Resources.py", title="Resources", icon=":material/share:"
    )

    coaching_message_board = st.Page(
        "layout/Coaching/7 Message Board.py", title="Message Board", icon=":material/forum:"
    )

    # Mental Health
    mental_health = st.Page(
        "layout/Mental Health/1 Mental Health.py", title="Mental Health", icon=":material/health_and_safety:"
    )

    mental_health_resources = st.Page(
        "layout/Mental Health/2 Resources and Support.py", title="Resources and Support", icon=":material/link:"
    )

    #Navigation
    pg = st.navigation(    {
            "Home": [home, how_to, external_links, club_shop],
            "Parent Info": [parent_info, parent_volunteering, parent_age_groups],
            "Player Info": [player_info],
            "Policies": [policies],
            "Safeguarding": [safeguarding, safeguarding_officers, safeguarding_ploicy],
            "Coaching": [coaches_handbook, coaching_team, coaching_juniors, coaching_athenas, coaching_minis, coaching_resources, coaching_message_board],
            "Mental Health": [mental_health, mental_health_resources]
        },
        expanded=True
    )

    #Sidebar
    if st.sidebar.button("Logout"):
        # Clear login state
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.rerun()
    st.sidebar.button("Send Feedback", on_click=show_feedback_form)
    st.sidebar.write("Version 0.3.0")

    pg.run()

def main():
    """Main application flow."""
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    
    # Check if user is logged in
    if not st.session_state['logged_in']:
        show_login_form()
    else:
        main_app()

# Run the app
if __name__ == "__main__":
    main()