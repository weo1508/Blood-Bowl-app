#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

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

st.text("Blood Bowl · " + st.session_state.currentPin)
st.subheader("You are all set!")

next = st.button("confirm and save", use_container_width=True)
role = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "role")

if next:
    m.updateDb(st.session_state.currentPin, "allSet", 1, "accountName", st.session_state.accountName)
    if role == "A":
        m.nextPage(next, "UIadmin4")
    else:
        m.nextPage(next, "UIplayerStart")