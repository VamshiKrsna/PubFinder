import streamlit as st
from streamlit import beta_container
from PIL import Image
import pandas as pd

st.title("GetHigh 🍻")  

st.markdown("Are you over 18 ? ")
sus = Image.open('Material\sus.jpg')
getin = Image.open('Material\getin.jpg')
home = Image.open('Material\home.jpg')

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