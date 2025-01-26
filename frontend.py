import subprocess
import streamlit as st

st.header("Tomb of the Ancient Kings", divider="rainbow")
st.subheader("What is Tomb of the Ancient Kings?")

st.markdown('''
    Tomb of the Ancient Kings is an old-school 2D rogue-lite game built entirely in python.
    It's a small project I created to help me learn python in a fun way.
            
    Cool features of Tomb of the Ancient Kings
    - Randomly generated dungeons, no 2 dungeons will be the same!
    - various monsters and items found within the world.
    - Infinite Levels! (Obviously)
            
    To try out the game simply hit the run button below

''')

if st.button("Run Game"):
    subprocess.run(["python3", "main.py"])

st.markdown('''

    Creator: Michael Giovannini
    [Source Code](https://github.com/Bardin0/rougue-lite)

''')