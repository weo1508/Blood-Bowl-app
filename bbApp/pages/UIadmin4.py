#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#mathcatsand. “Css Styling.” Streamlit, 26 Dec. 2022, discuss.streamlit.io/t/css-styling/35243. Accessed 30 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer4', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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

st.text("Blood Bowl · admin version · pre-game")
st.subheader("Current Game: " + st.session_state.currentPin)
st.text("")
st.text("")

st.columns([1,1,1], gap="small", vertical_alignment="top")
col1, col2, col3 = st.columns(3)

with col1:
    self = st.button("setup muself", use_container_width=True)
    m.nextPage(self, "UIplayer2")
with col2:
    set = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "allSet")
    if  set == 0:
        st.markdown("<h6 style='text-align: center;'>Set up your own stats before starting</h1>", unsafe_allow_html=True)
    else:
        start = st.button("start game", use_container_width=True)
        m.nextPage(start, "UIgame1")
with col3:
    back = st.button("back to login", use_container_width=True)
    m.nextPage(back, "UI")

