#CITATION
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer6', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("Weather")
st.text("Roll D6 for weather")

weather = st.text_input("weather", max_chars=20, value="weather", placeholder="weather", label_visibility="visible")
save = st.button("save and next", use_container_width=True)
if save:
    m.updateDb(st.session_state.currentPin, "weather", weather, "accountName", st.session_state.accountName)
    m.nextPage(save, "UIplayer7")
