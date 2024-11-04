#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer3', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("Game Code:")
st.subheader(st.session_state.currentPin)
st.text("")
st.text("")
st.text("")
st.text("let the players join this game with the code")
st.text("you can screenshot and share for convenience")

gotoNext = st.button("Next")
m.nextPage(gotoNext, "UIadmin4")