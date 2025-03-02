import streamlit as st

import random

st.title("Fluffy Guesser")
st.write("Which house is Fluffy in?")
st.write("If you don't know what Fluffy looks like, he looks like this: :material/flutter_dash:")
col1, col2, col3 = st.columns(3)
house = random.randint(1, 3)
with col1:
    st.image(image="house.png")
    b1 = st.button(label="The left house", icon=":material/home:")
with col2:
    st.image(image="house.png")
    b2 = st.button(label="The middle house", icon=":material/home:")
with col3:
    st.image(image="house.png")
    b3 = st.button(label="The right house", icon=":material/home:")
if b1:
    if house == 1:
        with col1:
            st.title(":material/flutter_dash:")
            st.write("Fluffy was in that house :)")
            st.write("Fluffy is now in another house")
            st.balloons()
    elif house != 1:
        with col1:
            st.write("Fluffy was not in that house :(")
            st.write("Fluffy is now in another house")
elif b2:
    if house == 2:
        with col2:
            st.title(":material/flutter_dash:")
            st.write("Fluffy was in that house :)")
            st.write("Fluffy is now in another house")
            st.balloons()
    elif house != 2:
        with col2:
            st.write("Fluffy was not in that house :(")
            st.write("Fluffy is now in another house")
elif b3:
    if house == 3:
        with col3:
            st.title(":material/flutter_dash:")
            st.write("Fluffy was in that house :)")
            st.write("Fluffy is now in another house")
            st.balloons()
    elif house != 3:
        with col3:
            st.write("Fluffy was not in that house :(")
            st.write("Fluffy is now in another house")
