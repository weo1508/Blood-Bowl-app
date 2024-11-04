#CITATION
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer5', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("Fans")
st.text("Roll D3 for fans")

fan = st.number_input("fans", value=0, placeholder=0, label_visibility="hidden")

save = st.button("save and next", use_container_width=True)
if save:
    m.updateDb(st.session_state.currentPin, "fan", fan, "accountName", st.session_state.accountName)
    m.nextPage(save, "UIplayer6")