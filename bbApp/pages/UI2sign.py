#CITATION
#---. “Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/. Accessed 15 Oct. 2024.
#Coding Is Fun. “How to Create a Streamlit Multi-Page Web App.” Www.youtube.com, 24 July 2022, www.youtube.com/watch?v=YClmpnpszq8. Accessed 10 Oct. 2024.
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

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

gotoNext = st.button("REGISTER")

if gotoNext:
    check = m.logCheckExist(name)
    if len(name) > 0 and len(password) > 0 and not name.isspace() and not password.isspace():
        if len(name) > 20 or len(password) > 20:
            message = "name or password too long, please enter under 20 characters"
            name = m.errorMessage(gotoNext, message)
            if 'accountName' not in st.session_state:
                st.session_state.accountName = name
            st.session_state.accountName = name
        elif check == True:
            message = "account name already taken, please choose a different one"
            m.errorMessage(gotoNext, message)
        else:
            if 'accountName' not in st.session_state:
                st.session_state['accountName'] = name
            m.sign(name, password, gotoNext)

