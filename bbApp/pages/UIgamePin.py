#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIgamePin', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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

inputPin = str(st.text_input("Enter pin in the format 000-000", value="000-000", placeholder='111-111'))
gotoNext = st.button("Next")

if gotoNext:
    if len(inputPin) == 7 and inputPin[3] == "-":
        check = m.checkPin(inputPin)
        if check == True:
            m.nextPage(gotoNext, "UIplayer2")
        else:
            message = "wrong pin, please reenter"
            m.errorMessage(gotoNext, message)
    else:
        message = "wrong format, please reenter"
        m.errorMessage(gotoNext, message)