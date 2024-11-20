#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#Streamlit. “How to Make a Timer?” Streamlit, 2 Mar. 2022, discuss.streamlit.io/t/how-to-make-a-timer/22675. Accessed 30 Oct. 2024.
#Streamlit. “Colored Text.” Streamlit, 17 Dec. 2022, discuss.streamlit.io/t/colored-text/34892. Accessed 30 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIgame1', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("Game Recording")
TD = st.number_input("TD", value=0, placeholder=0, label_visibility="visible")
st.text("")
Cas = st.number_input("Cas", value=0, placeholder=0, label_visibility="visible")
st.text("")

st.subheader("Timer")


# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
countdown_placeholder = st.empty()
initial_seconds = 180
countdown_placeholder.markdown(f"<h1 style='text-align: center; color: green;'>3:00</h1>", unsafe_allow_html=True)

total_seconds = initial_seconds
running = False

col1, col2 = st.columns(2)

with col1:
    if st.button("Start", use_container_width=True):
        if not running:
            running = True
            m.countdown()

with col2:
    if st.button("Reset", use_container_width=True):
        running = False
        total_seconds = initial_seconds
        countdown_placeholder.markdown(f"<h1 style='text-align: center; color: green;'>3:00</h1>",unsafe_allow_html=True)

st.text("")
st.subheader("View Stats")
view = st.button(label="Click to View", key=None, on_click=None, use_container_width=True)
m.nextPage(view, "UIgame2")

st.text("")
st.text("")
st.text("exit game and save stat, once exit you will be back to login page")
save = st.button("save and exit", use_container_width=False)

if save:
    m.updateDb(st.session_state.currentPin, "TD", TD, "accountName", st.session_state.accountName)
    m.updateDb(st.session_state.currentPin, "CAS", Cas, "accountName", st.session_state.accountName)
    m.nextPage(save, "UI")
