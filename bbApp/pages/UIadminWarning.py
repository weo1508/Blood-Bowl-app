#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIadminWarning', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.header(":red[WARNING]")
st.text("you should not exit the admin game setup page before completing the whole game setup")
st.text("you can modify the setup later but it will cause data loss if you exit while creating a new game")
st.text("")
st.text("")
st.text("")

ok = st.button(label="OK", key=None, on_click=None, use_container_width=False)

m.createPin(ok, "UIadmin2")
