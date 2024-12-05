import streamlit as st

# Display the banner image and the main title of the page
st.image("images/coaching/banner.png")
st.title("Coaching Team")

### Seniors Section
st.subheader("Seniors")

# Men coaches
with st.expander("Men", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Tom Bowen-Hall")
    with right_col:
        st.write("Rich Shacklock")

# Women coaches
with st.expander("Womens", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Amy Wheeler")
    with right_col:
        st.write("Ellie Rich")

### Juniors Section
st.subheader("Juniors")

# Colts coaches
with st.expander("Colts", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Ben Phillips")
    with right_col:
        st.write("Derek Goulding")

# Under 16's coaches
with st.expander("Under 16's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("???")
    with right_col:
        st.write("???")

# Under 15's coaches
with st.expander("Under 15's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("???")
    with right_col:
        st.write("???")

# Under 14's coaches
with st.expander("Under 14's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("???")
    with right_col:
        st.write("???")

# Under 13's coaches
with st.expander("Under 13's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("???")
    with right_col:
        st.write("???")

### Athenas Section
st.subheader("Athenas")

# Under 16s coaches
with st.expander("Under 16s", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Neil Ward")
    with right_col:
        st.write("Gary")

# Under 14's coaches
with st.expander("Under 14's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Liam O'Laughlon")
    with right_col:
        st.write("Chris Deane")

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
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Tom Lovell")
    with right_col:
        st.write("Alex Bridge")

# Under 11's coaches
with st.expander("Under 11's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Boc")
        st.divider()
        st.write("Hoff")
    with right_col:
        st.write("Tom Williams")
        st.divider()
        st.write("Sadie-May Powell")

# Under 10's coaches
with st.expander("Under 10's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Chris Broome")
    with right_col:
        st.write("James Peters")

# Under 9's coaches
with st.expander("Under 9's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("???")
    with right_col:
        st.write("???")

# Under 8's coaches
with st.expander("Under 8's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("???")
    with right_col:
        st.write("???")

# Under 7's coaches
with st.expander("Under 7's", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Mike Gibbs")
    with right_col:
        st.write("Sophie")

# Micros coaches
with st.expander("Micros", icon=":material/info:"):
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("Phoebe Rich")
    with right_col:
        st.write("Mia Jeremy")
