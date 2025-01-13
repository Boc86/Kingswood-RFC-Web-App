import streamlit as st
import supabase
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Initialize Supabase client
supabase_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

# Set up coaches
senior_coaches = supabase_client.table('members').select('*').eq( "age_group", 'seniors').order('last_name', desc=False).execute()
women_coaches = supabase_client.table('members').select('*').eq( "age_group", 'womens').order('last_name', desc=False).execute()
#walkers_coaches = supabase_client.table('members').select('*').eq( "age_group", 'walkers').order('last_name', desc=False).execute()
#air = supabase_client.table('members').select('*').eq( "age_group", 'air').order('last_name', desc=False).execute()
colts = supabase_client.table('members').select('*').eq( "age_group", 'colts').order('last_name', desc=False).execute()
aunder16s = supabase_client.table('members').select('*').eq( "age_group", 'a under 16s').order('last_name', desc=False).execute()
aunder14s = supabase_client.table('members').select('*').eq( "age_group", 'a under 14s').order('last_name', desc=False).execute()
aunder12s = supabase_client.table('members').select('*').eq( "age_group", 'a under 12s').order('last_name', desc=False).execute()

under16s = supabase_client.table('members').select('*').eq( "age_group", 'under 16s').order('last_name', desc=False).execute()
under15s = supabase_client.table('members').select('*').eq( "age_group", 'under 15s').order('last_name', desc=False).execute()
under14s = supabase_client.table('members').select('*').eq( "age_group", 'under 14s').order('last_name', desc=False).execute()
under13s = supabase_client.table('members').select('*').eq( "age_group", 'under 13s').order('last_name', desc=False).execute()
under12s = supabase_client.table('members').select('*').eq( "age_group", 'under 12s').order('last_name', desc=False).execute()
under11s = supabase_client.table('members').select('*').eq( "age_group", 'under 11s').order('last_name', desc=False).execute()
under10s = supabase_client.table('members').select('*').eq( "age_group", 'under 10s').order('last_name', desc=False).execute()
under9s = supabase_client.table('members').select('*').eq( "age_group", 'under 9s').order('last_name', desc=False).execute()
under8s = supabase_client.table('members').select('*').eq( "age_group", 'under 8s').order('last_name', desc=False).execute()
under7s = supabase_client.table('members').select('*').eq( "age_group", 'under 7s').order('last_name', desc=False).execute()
micros = supabase_client.table('members').select('*').eq( "age_group", 'micros').order('last_name', desc=False).execute()

# Display the banner image and the main title of the page
st.image("images/coaching/banner.png")
st.title("Coaching Team")
st.write("Meet the Kingswood Coaching Team")

### Seniors Section
st.subheader("Seniors")

# Men coaches
with st.expander("Mens", icon=":material/info:"):
    i = 0
    for rows in senior_coaches.data:
        st.subheader(str(senior_coaches.data[i]['first_name']) + " " + str(senior_coaches.data[i]['last_name']))
        st.write(str(senior_coaches.data[i]['title']))
        st.write("---")
        i += 1

# Women coaches
with st.expander("Womens", icon=":material/info:"):
    i = 0
    for rows in women_coaches.data:
        st.subheader(str(women_coaches.data[i]['first_name']) + " " + str(women_coaches.data[i]['last_name']))
        st.write(str(women_coaches.data[i]['title']))
        st.write("---")
        i += 1

with st.expander("Walking Rugby", icon=":material/directions_walk:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Steve Deery")
    with right_col:
        st.empty()

#AIR Section
st.subheader("All Inclusive Rugby")

with st.expander("AIR", icon=":material/all_inclusive:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Austin Coombs")
    with right_col:
        st.empty()

### Juniors Section
st.subheader("Juniors")

# Colts coaches
with st.expander("Colts", icon=":material/info:"):
    i = 0
    for rows in colts.data:
        st.subheader(str(colts.data[i]['first_name']) + " " + str(colts.data[i]['last_name']))
        st.write(str(colts.data[i]['title']))
        st.write("---")
        i += 1

# Under 16's coaches
with st.expander("Under 16s", icon=":material/info:"):
    i = 0
    for rows in under16s.data:
        st.subheader(str(under16s.data[i]['first_name']) + " " + str(under16s.data[i]['last_name']))
        st.write(str(under16s.data[i]['title']))
        st.write("---")
        i += 1

# Under 15's coaches
with st.expander("Under 15s", icon=":material/info:"):
    i = 0
    for rows in under15s.data:
        st.subheader(str(under15s.data[i]['first_name']) + " " + str(under15s.data[i]['last_name']))
        st.write(str(under15s.data[i]['title']))
        st.write("---")
        i += 1

# Under 14's coaches
with st.expander("Under 14s", icon=":material/info:"):
    i = 0
    for rows in under14s.data:
        st.subheader(str(under14s.data[i]['first_name']) + " " + str(under14s.data[i]['last_name']))
        st.write(str(under14s.data[i]['title']))
        st.write("---")
        i += 1

# Under 13's coaches
with st.expander("Under 13s", icon=":material/info:"):
    i = 0
    for rows in under13s.data:
        st.subheader(str(under13s.data[i]['first_name']) + " " + str(under13s.data[i]['last_name']))
        st.write(str(under13s.data[i]['title']))
        st.write("---")
        i += 1

### Athenas Section
st.subheader("Athenas")

# Under 16s coaches
with st.expander("Under 16s", icon=":material/info:"):
    i = 0
    for rows in aunder16s.data:
        st.subheader(str(aunder16s.data[i]['first_name']) + " " + str(aunder16s.data[i]['last_name']))
        st.write(str(aunder16s.data[i]['title']))
        st.write("---")
        i += 1

# Under 14's coaches
with st.expander("Under 14s", icon=":material/info:"):
    i = 0
    for rows in aunder14s.data:
        st.subheader(str(aunder14s.data[i]['first_name']) + " " + str(aunder14s.data[i]['last_name']))
        st.write(str(aunder14s.data[i]['title']))
        st.write("---")
        i += 1

# Under 12's coaches
with st.expander("Under 12's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Luke James")
    with right_col:
        st.write("Boc")

### Minis Section
st.subheader("Minis")

# Under 12s coaches
with st.expander("Under 12s", icon=":material/info:"):
    i = 0
    for rows in under12s.data:
        st.subheader(str(under12s.data[i]['first_name']) + " " + str(under12s.data[i]['last_name']))
        st.write(str(under12s.data[i]['title']))
        st.write("---")
        i += 1

# Under 11's coaches
with st.expander("Under 11s", icon=":material/info:"):
    i = 0
    for rows in under11s.data:
        st.subheader(str(under11s.data[i]['first_name']) + " " + str(under11s.data[i]['last_name']))
        st.write(str(under11s.data[i]['title']))
        st.write("---")
        i += 1

# Under 10's coaches
with st.expander("Under 10s", icon=":material/info:"):
    i = 0
    for rows in under10s.data:
        st.subheader(str(under10s.data[i]['first_name']) + " " + str(under10s.data[i]['last_name']))
        st.write(str(under10s.data[i]['title']))
        st.write("---")
        i += 1

# Under 9's coaches
with st.expander("Under 9s", icon=":material/info:"):
    i = 0
    for rows in under9s.data:
        st.subheader(str(under9s.data[i]['first_name']) + " " + str(under9s.data[i]['last_name']))
        st.write(str(under9s.data[i]['title']))
        st.write("---")
        i += 1

# Under 8's coaches
with st.expander("Under 8s", icon=":material/info:"):
    i = 0
    for rows in under8s.data:
        st.subheader(str(under8s.data[i]['first_name']) + " " + str(under8s.data[i]['last_name']))
        st.write(str(under8s.data[i]['title']))
        st.write("---")
        i += 1

# Under 7's coaches
with st.expander("Under 7s", icon=":material/info:"):
    i = 0
    for rows in under7s.data:
        st.subheader(str(under7s.data[i]['first_name']) + " " + str(under7s.data[i]['last_name']))
        st.write(str(under7s.data[i]['title']))
        st.write("---")
        i += 1

# Micros coaches
with st.expander("Micros", icon=":material/info:"):
    i = 0
    for rows in micros.data:
        st.subheader(str(micros.data[i]['first_name']) + " " + str(micros.data[i]['last_name']))
        st.write(str(micros.data[i]['title']))
        st.write("---")
        i += 1
