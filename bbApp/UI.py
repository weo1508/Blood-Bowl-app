#CITATION
#---. “Text Elements - Streamlit Docs.” Streamlit.io, 2024, docs.streamlit.io/develop/api-reference/text. Accessed 15 Oct. 2024.
#Coding Is Fun. “How to Create a Streamlit Multi-Page Web App.” Www.youtube.com, 24 July 2022, www.youtube.com/watch?v=YClmpnpszq8. Accessed 10 Oct. 2024.
#Charly_Wargnier. “How to Move Elements to Other Positions.” Streamlit, May 2024, discuss.streamlit.io/t/how-to-move-elements-to-other-positions/68380/2. Accessed 20 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'LOG IN', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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


#st.sidebar.success("Select a demo above.")

st.title("Welcome to Blood Bowl")

logIn = st.button(label="Log In", key=None, on_click=None, use_container_width=True)
st.text("No account yet? Sign up --------->")
st.text("")
signUp = st.button(label="Sign Up", key=None, on_click=None, use_container_width=True)


m.nextPage(logIn,"UI2log")
m.nextPage(signUp,"UI2sign")
