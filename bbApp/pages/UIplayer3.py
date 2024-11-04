#CITATION
#Streamlit. “Session State - Streamlit Docs.” Docs.streamlit.io, 2024, docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state. Accessed 15 Oct. 2024.

import streamlit as st
import methods as m

st.set_page_config(page_title= 'UIplayer3', layout="wide", initial_sidebar_state="collapsed", menu_items=None)

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
st.subheader("select race")
raceOptions = ["Amazon", "Black Orc", "Bretonnian", "Chaos Chosen", "Chaos Dwarf", "Chaos Halfling", "Chaos Renegades", "Dark Elf", "Dwarf", "Elven Union", "Ethereal", "Goblin", "Halfling", "High Elf", "Hobgoblin Slaver", "Human", "Imperial Nobility", "Khorne", "Khorne Daemons", "Kislev Circus", "Lizardmen", "Necromantic Horror", "Night Goblin", "Norse - OWC", "Norse - Chaos Undivi", "Norse - Chaos Undivi", "Nurgle", "Nurglings", "Ogre", "Old World Alliance", "Orc", "Pestilent Vermin", "Savage Orc", "Shambling Undead", "Skaven", "Slaanesh", "Slaaneshi Daemons", "Slann", "Slayer Hold", "Snotling", "Squig", "Squirrels", "Tomb Kings", "Tzeentch", "Tzeentch Daemons", "Underworld Denizens", "Union of Small People", "Vampire", "Von Carsteins", "Wood Elf"]
selectRace = st.selectbox("select race", raceOptions, index=0, placeholder="select race", label_visibility="hidden")

save = st.button("save and next", use_container_width=True)
if save:
    m.updateDb(st.session_state.currentPin, "race", selectRace, "accountName", st.session_state.accountName)
    m.nextPage(save, "UIplayer4")

