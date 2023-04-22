import streamlit as st
from PIL import Image
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_PATH = os.path.join(BASE_DIR, 'Material', 'sus.jpg')
GETIN = os.path.join(BASE_DIR, 'Material', 'getin.jpg') 
HOME = os.path.join(BASE_DIR, 'Material', 'home.jpg')

sus = Image.open(IMAGE_PATH)
getin = Image.open(GETIN)
home = Image.open(IMAGE_PATH)

st.markdown("Are you over 18 ? ")
st.image(sus)
button = st.button("Hell Yeah !")

df = pd.read_csv("open_pubs.csv")


if button == True:
        st.image(getin)
        st.markdown("Have Fun champ")
        st.markdown("Help Yourself going through this list :")
        st.dataframe(df)

if st.button("Nope, I'm Underage"):
        st.image(home)
        st.markdown("Go Do Your Homework")
