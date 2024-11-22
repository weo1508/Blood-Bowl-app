#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#mathcatsand. “Css Styling.” Streamlit, 26 Dec. 2022, discuss.streamlit.io/t/css-styling/35243. Accessed 30 Oct. 2024.
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIadminDisplay', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader(str(st.session_state.viewPin) + " · " + str(st.session_state.viewName))

st.columns([1,1,1], gap="small", vertical_alignment="top")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h5 style='text-align: left;'>Race</h1>", unsafe_allow_html=True)
    race = m.getFromDb(st.session_state.viewPin, "name", st.session_state.viewName, "race")
    if race is None:
        st.text("no selection")
    else:
        st.text(race)
    st.text("")
    st.markdown("<h5 style='text-align: left;'>Players</h1>", unsafe_allow_html=True)
    for i in range(16):
        player = m.getFromDb(st.session_state.viewPin, "name", st.session_state.viewName, "p" + str(i+1))
        if player is None:
            if i == 0:
                st.text("no selection")
                break
            else:
                break
        else:
            st.text(str(player))

with col2:
    st.markdown("<h5 style='text-align: left;'>Fan</h1>", unsafe_allow_html=True)
    fan = m.getFromDb(st.session_state.viewPin, "name", st.session_state.viewName, "fan")
    if fan is None:
        st.text("no selection")
    else:
        st.text(str(fan))
    st.text("")

    st.markdown("<h5 style='text-align: left;'>Weather</h1>", unsafe_allow_html=True)
    weather = m.getFromDb(st.session_state.viewPin, "name", st.session_state.viewName, "weather")
    if weather is None:
        st.text("no selection")
    else:
        st.text(str(weather))
    st.text("")

    st.markdown("<h5 style='text-align: left;'>Treasury</h1>", unsafe_allow_html=True)
    treasury = m.getFromDb(st.session_state.viewPin, "name", st.session_state.viewName, "treasury")
    if treasury is None:
        st.text("no selection")
    else:
        st.text(str(treasury))

with col3:
    st.markdown("<h5 style='text-align: left;'>TD</h1>", unsafe_allow_html=True)

    st.text("")
    st.markdown("<h5 style='text-align: left;'>Cas</h1>", unsafe_allow_html=True)


back = st.button(label="back", key=None, on_click=None, use_container_width=False)
m.nextPage(back, "UIadminView2")
