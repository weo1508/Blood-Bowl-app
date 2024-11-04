#CITATION
##---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'LOG IN', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown(
    """
    <style>
    .stSidebar {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to Blood Bowl")
player = st.button(label="Begin as Player", key=None, on_click=None, use_container_width=False)
st.text("Admin/Host? Click here")
admin = st.button(label="Begin as Admin", key=None, on_click=None, use_container_width=False)

m.nextPage(player, "UIplayer1")
m.nextPage(admin, "UIadmin1")