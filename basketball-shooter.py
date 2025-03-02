import streamlit as st

from streamlit_image_coordinates import streamlit_image_coordinates as st_im_coords

from PIL import Image

st.title("Basketball Shooter")
st.write("Click on the basketball hoop to shoot.")
location = st_im_coords(
    Image.open("basketball-hoop.png"),
    width=250,
    key="png",
)
st.write(location)
arc = st.slider("Use the slider to change the arc of your shot.", 0, 15)
