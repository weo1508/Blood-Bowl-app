#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#Streamlit. “How to Make a Timer?” Streamlit, 2 Mar. 2022, discuss.streamlit.io/t/how-to-make-a-timer/22675. Accessed 30 Oct. 2024.
#Streamlit. “Colored Text.” Streamlit, 17 Dec. 2022, discuss.streamlit.io/t/colored-text/34892. Accessed 30 Oct. 2024.

import streamlit as st
import methods as m
from streamlit.components.v1 import html

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
my_html = """
<script>
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}

window.onload = function () {
    var threeMinutes = 60 * 3,
        display = document.querySelector('#time');
    startTimer(threeMinutes, display);
};
</script>

<body>
  <style>
    #time {
        font-size: large; /* Adjust size as needed */
        color: #3CB043; /* Change color as needed */
        text-align: left;
    }
  </style>
  <div><span id="time">03:00</span></div>
</body>
"""

html(my_html)


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
