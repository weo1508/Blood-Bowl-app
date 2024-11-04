#CITATION
##---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIadmin1', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.text("")
#st.write(st.session_state.accountName)

st.subheader("Admin Functions")
create = st.button(label="Creat New Game", key=None, on_click=None, use_container_width=False)
view = st.button(label="View Player Stats", key=None, on_click=None, use_container_width=False)

st.text("")
st.subheader("General Function")
join = st.button(label="Join Game", key=None, on_click=None, use_container_width=False)

m.createPin(create, "UIadminWarning")
m.nextPage(view, "UIadminView")

m.nextPage(join, "UIgamePin")