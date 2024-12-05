import streamlit as st
from streamlit_gsheets import GSheetsConnection as GSC
from forms.resource import resource_form
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/coaching/resources/intro.md')

conn = st.connection("gsheets", type=GSC)

df = conn.read(worksheet=1442126310, ttl=0)

@st.dialog("Share a resource")
def show_resource_form():
    resource_form()

st.title("Coaching Resources")
st.markdown(intro_markdown, unsafe_allow_html=True)

with st.container(height=650, border=True):
    for row in df.itertuples():
        st.markdown(f"**Title**: {row.resource}")
        st.markdown(f"**Link**: {row.link}")
        st.markdown(f"**Description**: {row.description}")
        st.write("---")

st.button("Share a resource", on_click=show_resource_form)