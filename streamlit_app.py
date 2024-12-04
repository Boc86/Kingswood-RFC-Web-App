import streamlit as st
from PIL import Image
from forms.feedback import feddback_form

@st.dialog("Send Feedback")
def show_feedback_form():
    feddback_form()


icon = Image.open('images/logo.png')

st.set_page_config(
    page_title="KRFC Volunteers Community",
    page_icon="🏉",
    layout="wide"
)

st.logo(
    image=Image.open('images/logo.png'),
    link="https://www.kingswoodrfc.co.uk",
    size="large",
    icon_image=Image.open('images/icon.png')
)

### Home ###
home = st.Page(
    "layout/Home/1 Home.py", title="Home", icon=":material/home:", default= True
)

how_to = st.Page(
    "layout/Home/2 HowTo.py", title="How to use the Kingswood RFC Volunteer Community Web App", icon=":material/help:"
)

external_links = st.Page(
    "layout/Home/3 External Links,py", title="External Links", icon=":material/captive_portal:"
)

### Parent Info ###
parent_info = st.Page(
    "layout/Parent Info/1 Parent Info.py", title="Welcome Letter", icon=":material/info:"
)

parent_volunteering = st.Page(
    "layout/Parent Info/2 Parent Volunteering.py", title="Volunteering", icon=":material/volunteer_activism:"
)

parent_age_groups = st.Page(
    "layout/Parent Info/3 Parent Age Groups.py", title="Age Groups", icon=":material/pin:"
)

### Player Info ###
player_info = st.Page(
    "layout/Player Info/1 Player Info.py", title="Player Info", icon=":material/info:"
)

### Policies ###
policies = st.Page(
    "layout/Policies/1 Policies.py", title="Policies", icon=":material/topic:"
)

### Safeguarding ###
safeguarding = st.Page(
    "layout/Safeguarding/1 Safeguarding.py", title="Safeguarding", icon=":material/enhanced_encryption:"
)

safeguarding_officers = st.Page(
    "layout/Safeguarding/2 Safeguarding Officers.py", title="Safeguarding Officers", icon=":material/group:"
)

safeguarding_ploicy = st.Page(
    "layout/Safeguarding/3 Safeguarding Policy.py", title="Safeguarding Policy", icon=":material/description:"
)

### Coaching ###
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

coaching_resources = st.Page(
    "layout/Coaching/7 Message Board.py", title="Message Board", icon=":material/forum:"
)

### Mental Health ###
mental_health = st.Page(
    "layout/Mental Health/1 Mental Health.py", title="Mental Health", icon=":material/health_and_safety:"
)

mental_health_resources = st.Page(
    "layout/Mental Health/2 Resources and Support.py", title="Resources and Support", icon=":material/link:"
)

pg = st.navigation(
    {
        "Home": [home, how_to, external_links],
        "Parent Info": [parent_info, parent_volunteering, parent_age_groups],
        "Player Info": [player_info],
        "Policies": [policies],
        "Safeguarding": [safeguarding, safeguarding_officers, safeguarding_ploicy],
        "Coaching": [coaches_handbook, coaching_team, coaching_juniors, coaching_athenas, coaching_minis, coaching_resources],
        "Mental Health": [mental_health, mental_health_resources]
    }
)

st.sidebar.button("Send Feedback", on_click=show_feedback_form)

pg.run() 