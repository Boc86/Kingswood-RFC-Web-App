import streamlit as st

st.image("images/coaching/banner.png")
st.title("Coaching Team")

### Seniors
st.subheader("Sesniors")
with st.expander("Men", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Tom Bowen-Hall")
    
    with right_col:
        st.write("Rich Shacklock")

with st.expander("Womens", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Amy Wheeler")
    
    with right_col:
        st.write("Ellie Rich")
    
### Juniors
st.subheader("Juniors")
with st.expander("Colts", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Ben Phillips")
    
    with right_col:
        st.write("Derek Goulding")

with st.expander("Under 16's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("???")
    
    with right_col:
        st.write("???")

with st.expander("Under 15's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("???")
    
    with right_col:
        st.write("???")

with st.expander("Under 14's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("???")
    
    with right_col:
        st.write("???")

with st.expander("Under 13's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("???")
    
    with right_col:
        st.write("???")

### Athenas
st.subheader("Athenas")
with st.expander("Under 16s", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Neil Ward")
    
    with right_col:
        st.write("Gary")

with st.expander("Under 14's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Liam O'Laughlon")
    
    with right_col:
        st.write("Chris Deane")

with st.expander("Under 12's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Luke James")
    
    with right_col:
        st.write("Boc")

### Minis
st.subheader("Minis")
with st.expander("Under 12s", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Tom Lovell")
    
    with right_col:
        st.write("Alex Bridge")

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

with st.expander("Under 10's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Chris Broome")
    
    with right_col:
        st.write("James Peters")

with st.expander("Under 9's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("???")
    
    with right_col:
        st.write("???")

with st.expander("Under 8's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("???")
    
    with right_col:
        st.write("???")

with st.expander("Under 7's", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Mike Gibbs")
    
    with right_col:
        st.write("Sophie")

with st.expander("Micros", icon=":material/info:"):
    left_col, right_col = st.columns(2)

    with left_col:
        st.write("Phoebe Rich")
    
    with right_col:
        st.write("Mia Jeremy")