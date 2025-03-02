import streamlit as st

import random

st.title("Rock, Paper, Scissors")
st.write("Choose one:")
r_n = random.randint(1, 3)
r_c = "nothing"
p_c = "nothing"
p_n = 0
p_p = 0
r_p = 0
winner = "None of us are"
if r_n == 1:
    r_c = "Rock"
elif r_n == 2:
    r_c = "Paper"
elif r_n == 3:
    r_c = "Scissors"
co1l, co2l, co3l = st.columns(3)
with co1l:
    rock = st.button(label="Rock", icon=":material/hexagon:", use_container_width=True)
with co2l:
    paper = st.button(label="Paper", icon=":material/draft:", use_container_width=True)
with co3l:
    scissors = st.button(label="Scissors", icon=":material/content_cut:", use_container_width=True)
if rock:
    p_n = 1
    p_c = "Rock"
elif paper:
    p_n = 2
    p_c = "Paper"
elif scissors:
    p_n = 3
    p_c = "Scissors"
if p_n == 1 and r_n == 3:
    p_p += 1
elif p_n == 1 and r_n == 2:
    r_p += 1
elif p_n == 2 and r_n == 1:
    p_p += 1
elif p_n == 2 and r_n == 3:
    r_p += 1
elif p_n == 3 and r_n == 2:
    p_p += 1
elif p_n == 3 and r_n == 1:
    r_p += 1
if p_p > r_p:
    winner = "You are"
elif p_p < r_p:
    winner = "I am"
elif p_p == r_p:
    winner == "None of us are"
st.write(f"You chose {p_c} and I chose {r_c}. The score is {p_p}|{r_p}, {winner} winning.")
