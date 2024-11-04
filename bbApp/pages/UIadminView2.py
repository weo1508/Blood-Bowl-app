#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIadminView2', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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

st.text("Blood Bowl · admin version")
st.subheader("Choose a player to view:")
st.text("")

playerNum = m.getFromDb("track", "pin", st.session_state.currentPin, "playerNum")

fetch = m.getTableFromDb(st.session_state.currentPin)
if 'table' not in st.session_state:
    st.session_state['table'] = fetch

names = []

for i in range(playerNum):
    names.append(fetch[i][2])
    name = st.button(label=names[i], key="name" + str(i), on_click=None, use_container_width=True)
    if name:
        if 'viewName' not in st.session_state:
            st.session_state.viewName = names[i]
        st.session_state.viewName = names[i]
        m.nextPage(name, "UIadminDisplay")


st.text("")
back = st.button(label="back", key=None, on_click=None, use_container_width=False)
m.nextPage(back, "UIadminView1")


