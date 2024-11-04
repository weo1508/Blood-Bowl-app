#CITATION
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer4', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("Buy players")
st.text("input how many players you have and enter names below")

st.text("")
st.text("how many (at max 16):")
number = st.number_input("add/delete players", min_value=1, max_value=16, step=1, label_visibility="collapsed")

st.text("")
st.text("their names:")
names=[]
for i in range(number):
    name = st.text_input("name " + str(i + 1), max_chars=20, value="player" + str(i + 1), placeholder="player " + str(i + 1), label_visibility="visible")
    names.append(name)

toUpdate = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12", "p13", "p14", "p15", "p16"]

save = st.button("save and next", use_container_width=True)
if save:
    for i in range(number):
        m.updateDb(st.session_state.currentPin, toUpdate[i], names[i], "accountName", st.session_state.accountName)
    m.nextPage(save, "UIplayer5")

