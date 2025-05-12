#CITATION
#---. “Text Elements - Streamlit Docs.” Streamlit.io, 2024, docs.streamlit.io/develop/api-reference/text. Accessed 15 Oct. 2024.
#Coding Is Fun. “How to Create a Streamlit Multi-Page Web App.” Www.youtube.com, 24 July 2022, www.youtube.com/watch?v=YClmpnpszq8. Accessed 10 Oct. 2024.

import streamlit as st
import methods as m


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

st.subheader("account name:")
name = str(st.text_input("type in name here"))
st.subheader("password:")
password = str(st.text_input("type in password here"))

gotoNext = st.button("LOG IN")

name = m.log(name, password, gotoNext)

if 'accountName' not in st.session_state:
    st.session_state.accountName = name
st.session_state.accountName = name
