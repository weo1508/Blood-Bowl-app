#CITATION
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.
#“How do you hide the sidebar of streamlit multiple page website” prompt. ChatGPT, GPT-3.5 version, OpenAI, 30 Oct. 2024., chat.openai.com.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer1', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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

st.text("Blood Bowl · player version")
st.text("")

st.subheader("General Function")
join = st.button(label="Join Game", key=None, on_click=None, use_container_width=False)
m.nextPage(join, "UIgamePin")
