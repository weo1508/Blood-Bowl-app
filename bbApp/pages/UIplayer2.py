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
st.subheader("pick your name: ")

playerNum = m.getFromDb("track", "pin", st.session_state.currentPin, "playerNum")


names = m.getNameFromDb(st.session_state.currentPin, "accountName", "name")
role = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "role")


if role == "A":
    adminName = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "name")
    st.text("detected that you are admin, confirm your name:")
    confirm = st.button(str(adminName), use_container_width=True)
    m.nextPage(confirm, "UIplayer3")
else:
    selectName = st.selectbox("select name", names, index=0, placeholder="pick your name", label_visibility="hidden")
    confirm = st.button("confirm", use_container_width=True)
    if confirm:
        m.updateDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "name", selectName)
        m.nextPage(confirm, "UIplayer3")
