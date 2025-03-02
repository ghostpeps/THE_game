import streamlit as st

import streamlit_extras.stylable_container as st_extras

def THE_game():
    url = "https://ghostpeps.weebly.com/"
    st.title("Welcome to *THE* game")
    st.write("By: [ghostpeps](%s)" % url)
    st.write("Choose a game you would like to play:")
    with st_extras.stylable_container(
        "grey",
        css_styles="""
        button {
            background-color: #696B69;
            color: black;
        }""",
    ):
        rps_button = st.button(label="Rock, Paper, Scissors", key="rpsb", icon=":material/content_cut:", use_container_width=True)
    with st_extras.stylable_container(
        "light_orange",
        css_styles="""
        button {
            background-color: #D6AF5A;
            color: black;
        }""",
    ):
        guess_number = st.button(label="Guess the Number", icon=":material/123:", use_container_width=True)
    with st_extras.stylable_container(
        "snow_blue",
        css_styles="""
        button {
            background-color: #B3D0E6;
            color: black;
        }""",
    ):
        fluffy_button = st.button(label="Fluffy Guesser", icon=":material/flutter_dash:", use_container_width=True)
    with st_extras.stylable_container(
        "green",
        css_styles="""
        button {
            background-color: #0FA322;
            color: black;
        }""",
    ):
        bug_smasher = st.button(label="Bug Smasher", icon=":material/bug_report:", use_container_width=True)
    with st_extras.stylable_container(
        "orange",
        css_styles="""
        button {
            background-color: #EDA509;
            color: black;
        }""",
    ):
        basketball = st.button(label="Basketball Shooter", icon=":material/sports_basketball:", use_container_width=True)
    if rps_button:
        st.switch_page("rock_paper_scissors.py")
    if guess_number:
        st.switch_page("guess-the-number.py")
    if fluffy_button:
        st.switch_page("fluffy-guesser.py")
    if bug_smasher:
        st.switch_page("bug-smasher.py")
    if basketball:
        st.switch_page("basketball-shooter.py")
pgs = st.navigation([
    st.Page(page=THE_game, title="THE game", icon=":material/joystick:"),
    st.Page(page="rock_paper_scissors.py", title="Rock, Paper, Scissors", icon=":material/content_cut:"),
    st.Page(page="guess-the-number.py", title="Guess the Number", icon=":material/123:"),
    st.Page(page="fluffy-guesser.py", title="Fluffy Guesser", icon=":material/flutter_dash:"),
    st.Page(page="bug-smasher.py", title="Bug Smasher", icon=":material/bug_report:"),
    st.Page(page="basketball-shooter.py", title="Basketball Shooter", icon=":material/sports_basketball:")
])
pgs.run()
