import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
from PIL import Image

icon = Image.open('images/logo.png')

st.set_page_config(
    page_title="KRFC Volunteers Community",
    page_icon="🏉",
    layout="wide"
)

st.logo(
    icon,
    link="https://www.kingswoodrfc.co.uk",
    size="large"
)

### Home ###
home = st.Page(
    "layout/Home/1 Home.py", title="Home", icon="🏡", default= True
)

how_to = st.Page(
    "layout/Home/2 HowTo.py", title="How to use the Kingswood RFC Volunteer Community Web App", icon="❓"
)

### Parent Info ###
parent_info = st.Page(
    "layout/Parent Info/1 Parent Info.py", title="Parent Info", icon="ℹ️"
)

### Player Info ###
player_info = st.Page(
    "layout/Player Info/1 Player Info.py", title="Player Info", icon="ℹ️"
)

### Policies ###
policies = st.Page(
    "layout/Policies/1 Policies.py", title="Policies", icon="📁"
)

### Safeguarding ###
safeguarding = st.Page(
    "layout/Safeguarding/1 Safeguarding.py", title="Safeguarding", icon="👷"
)

### Coaching ###
coaching = st.Page(
    "layout/Coaching/1 Coaching.py", title="Coaching", icon="🚌"
)
coaching_team = st.Page(
    "layout/Coaching/2 Coaching Team.py", title="Coaching Team", icon="🤼"
)

### Mental Health ###
mental_health = st.Page(
    "layout/Mental Health/1 Mental Health.py", title="Mental Health", icon="⛑️"
)

pg = st.navigation(
    {
        "Home": [home, how_to],
        "Parent Info": [parent_info],
        "Player Info": [player_info],
        "Policies": [policies],
        "Safeguarding": [safeguarding],
        "Coaching": [coaching, coaching_team],
        "Mental Health": [mental_health]
    }
)

pg.run()