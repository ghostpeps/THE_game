import streamlit as st

import random

st.title("Guess the Number")
p_c = st.selectbox(
    label="Chose a difficulty:",
    options=("Easy", "Normal", "Hard", "Extreme"),
    placeholder="Chose a difficulty..."
)
s_n = 0
b_n = 0
pg = 0
r_n = 0
col1, col2 = st.columns(2)
if p_c == "Easy":
    s_n = 1
    b_n = 10
elif p_c == "Normal":
    s_n = 1
    b_n = 50
elif p_c == "Hard":
    s_n = 1
    b_n = 100
elif p_c == "Extreme":
    s_n = 1
    b_n = 1000
r_n = random.randint(s_n, b_n)
with col1:
    pg = st.number_input(label=f"Guess a number {s_n} to {b_n}:", min_value=s_n, max_value=b_n, value=1, step=1, placeholder=f"Guess a number {s_n} to {b_n}...")
with col2:
    confirm = st.button(label="Guess", icon=":material/check:", use_container_width=True)
if confirm:
    pg_confirmed = pg
    if pg_confirmed == r_n:
        st.write("You guessed the number!")
        st.balloons()
    elif pg_confirmed > r_n:
        st.write("The number you guessed is bigger than the number I am thinking of.")
    elif pg_confirmed < r_n:
        st.write("The number you guessed is smaller than the number I am thinking of.")
