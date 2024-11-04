#CITATION
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer2', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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

st.text("Blood Bowl · player version · " + st.session_state.currentPin)

st.columns([1,1], gap="small", vertical_alignment="top")
col1, col2 = st.columns(2)

with col1:
    start = st.button("start game", use_container_width=True)
    m.nextPage(start, "UIgame1")
with col2:
    back = st.button("back to login", use_container_width=True)
    m.nextPage(back, "UI")