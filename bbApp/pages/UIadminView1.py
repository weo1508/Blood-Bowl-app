#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIadminView1', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("Choose a game to view:")
st.text("")

pins = []
rows = m.countRows("track")
st.write(rows)

fetch = m.getTableFromDb("track")

for i in range(rows-1):
    pins.append(fetch[i][0])
    viewChoice = st.button(label=str(pins[i]), key="name" + str(i), on_click=None, use_container_width=True)
    if viewChoice:
        if 'viewPin' not in st.session_state:
            st.session_state['viewPin'] = pins[i]
        st.session_state.viewPin = pins[i]
        check = m.getFromDb(st.session_state.viewPin, "accountName", "role")
        if check = "A":
            m.nextPage(viewChoice, "UIadminView2")
        else:
            st.write("You are not the admin of this game.")

st.text("")
back = st.button(label="back", key=None, on_click=None, use_container_width=False)
m.nextPage(back, "UIadmin1")


