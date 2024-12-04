import streamlit as st
from streamlit_gsheets import GSheetsConnection as GSC
from forms.message import message_form
from funcs.read_markdown import read_markdown_file

intro_markdown = read_markdown_file('content/coaching/message board/intro.md')

conn = st.connection("gsheets", type=GSC)

df = conn.read(ttl=0)

@st.dialog("Submit a message")
def show_message_form():
    message_form()

st.title("Message Board")
st.markdown(intro_markdown, unsafe_allow_html=True)

with st.container(height=650, border=True):
    for row in df.itertuples():
        st.markdown(f"**Posted by**: {row.name} @ {row.date}")
        st.markdown(f"**Message**: {row.message}")

st.button("Submit a message", on_click=show_message_form)