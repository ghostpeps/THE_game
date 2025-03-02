import streamlit as st

import random

url = "https://www.extermpro.com/household-products-that-can-kill-pests/#:~:text=Windex%20%E2%80%93%20Windex%20is%20one%20of,them%20within%20a%20few%20moments"
st.markdown("""
<style>
.small-font {
    font-size:11px !important;
}
</style>
""", unsafe_allow_html=True)
st.title("Bug Smasher")
c1, c2 = st.columns(2)
with c1:
    st.write("Click on the bug to kill it using Windex*")
with c2:
    st.image(image="windex.png", width=100)
col1, col2, col3, col4, col5 = st.columns(5)
col6, col7, col8, col9, col10 = st.columns(5)
col11, col12, col13, col14, col15 = st.columns(5)
col16, col17, col18, col19, col20 = st.columns(5)
col21, col22, col23, col24, col25 = st.columns(5)
spot = random.randint(1, 25)
if spot == 1:
    with col1:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 2:
    with col2:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 3:
    with col3:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 4:
    with col4:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 5:
    with col5:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 6:
    with col6:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 7:
    with col7:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 8:
    with col8:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 9:
    with col9:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 10:
    with col10:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 11:
    with col11:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 12:
    with col12:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 13:
    with col13:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 14:
    with col14:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 15:
    with col15:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 16:
    with col16:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 17:
    with col17:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 18:
    with col18:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 19:
    with col19:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 20:
    with col20:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 21:
    with col21:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 22:
    with col22:
        bug = st.button(label="", type="tertiary", icon=":material/bug_report:")
elif spot == 23:
    with col23:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
elif spot == 24:
    with col24:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control_rodent:")
elif spot == 25:
    with col25:
        bug = st.button(label="", type="tertiary", icon=":material/pest_control:")
st.markdown('<p class="small-font">*Windex kills most pests, according to <a href=url>Household Products that Can Kill Pests · ExtermPRO</a>.</p>', unsafe_allow_html=True)
