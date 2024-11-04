#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#---. “St.columns - Streamlit Docs.” Streamlit.io, 2024, docs.streamlit.io/develop/api-reference/layout/st.columns. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIadmin2', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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

st.subheader("add players")
number = st.number_input("add players", min_value=2, max_value=10, step=1, label_visibility="collapsed")

st.text("")
st.text("")
st.subheader("name the players / set treasury / identify admin or player")
st.text("please select admin in the last column for your own name")

st.columns([1,1,1], gap="small", vertical_alignment="top")
col1, col2, col3 = st.columns(3)

names = []
treasury = []
roles = []
selectRole = ["Player", "Admin"]

with col1:
    for i in range(number):
        name = st.text_input("player " + str(i+1), max_chars=20, value="player" + str(i+1), placeholder="player " + str(i+1), label_visibility="visible")
        names.append(name)

with col2:
    for i in range(number):
        treasuryP = st.number_input("player " + str(i+1), value=0, placeholder=0, label_visibility="hidden")
        treasury.append(treasuryP)

with col3:
    for i in range(number):
        role = st.selectbox("player " + str(i+1), selectRole, index=0, placeholder="Player/Admin", label_visibility="hidden")
        if role == "Player":
            roles.append("P")
        elif role == "Admin":
            roles.append("A")

next = st.button(label="Next")
passCheck = m.UIadmin2PassCheck(roles)

if next:
    if passCheck:
        col = ["name", "treasury", "role", "firstLog", "allSet"]
        for i in range(number):
            toInsert = [names[i], treasury[i], roles[i], 0, 0]
            m.addToDb(st.session_state.currentPin, col, toInsert)
            m.updateDb("track", "playerNum", number, "pin", st.session_state.currentPin)
        m.updateDb(st.session_state.currentPin, "accountName", st.session_state.accountName, "role", "A")
        m.nextPage(next, "UIadmin3")
    else:
        st.text("You need to identify one admin.")
