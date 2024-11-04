import streamlit as st
import time
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

st.text("Blood Bowl · " + str(st.session_state.currentPin))
st.subheader(str(st.session_state.viewPin) + " · " + str(st.session_state.viewName))

st.columns([1,1], gap="small", vertical_alignment="top")
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h5 style='text-align: left;'>Race</h1>", unsafe_allow_html=True)
    race = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "race")
    if race is None:
        st.text("no selection")
    else:
        st.text(race)
    st.text("")
    st.markdown("<h5 style='text-align: left;'>Players</h1>", unsafe_allow_html=True)
    for i in range(16):
        player = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "p" + str(i+1))
        if player is None:
            st.text("no selection")
            break

with col2:
    st.markdown("<h5 style='text-align: left;'>Fan</h1>", unsafe_allow_html=True)
    fan = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "fan")
    if fan is None:
        st.text("no selection")
    else:
        st.text(str(fan))
    st.text("")

    st.markdown("<h5 style='text-align: left;'>Weather</h1>", unsafe_allow_html=True)
    weather = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "weather")
    if weather is None:
        st.text("no selection")
    else:
        st.text(str(weather))
    st.text("")

    st.markdown("<h5 style='text-align: left;'>Treasury</h1>", unsafe_allow_html=True)
    treasury = m.getFromDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "treasury")
    if treasury is None:
        st.text("no selection")
    else:
        st.text(str(treasury))


back = st.button(label="back", key=None, on_click=None, use_container_width=False)
m.nextPage(back, "UIgame1")
