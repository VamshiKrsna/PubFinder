import streamlit as st
from streamlit import beta_container
from PIL import Image
import pandas as pd
import folium
from geopy.geocoders import Nominatim
import math



def home():
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


def pubs():
    df = pd.read_csv('open_pubs.csv')

    st.title("Pubs 🍻")

    selected_postal_code = st.selectbox('Select a postal code', df['PostalCode'].unique())
    selected_latitude = df.loc[df['PostalCode'] == selected_postal_code, 'Latitude'].iloc[0]
    selected_longitude = df.loc[df['PostalCode'] == selected_postal_code, 'Longitude'].iloc[0]

    selected_pubs = df.loc[df['PostalCode'] == selected_postal_code]

    map = folium.Map(location=[selected_latitude, selected_longitude], zoom_start=10)

    for index, row in selected_pubs.iterrows():
        popup_html = '<b>' + row['Name'] + '</b><br>' + row['Address']
        marker = folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup_html, icon = folium.Icon(color = 'red'))
        marker.add_to(map)

    st.components.v1.html(map._repr_html_(), width=700, height=500)

def findpubs():
    df = pd.read_csv('open_pubs.csv')

    st.title("Find Pubs 🍻")

    lat = st.number_input('Enter your latitude:')
    lon = st.number_input('Enter your longitude:')

    df['Distance'] = df.apply(lambda row: math.sqrt((lat - row['Latitude']) ** 2 + (lon - row['Longitude']) ** 2), axis=1)

    nearest_pubs = df.nsmallest(5, 'Distance')

    map = folium.Map(location=[lat, lon], zoom_start=12)

    user_marker = folium.Marker(location=[lat, lon], popup='Your Location')
    user_marker.add_to(map)

    for index, row in nearest_pubs.iterrows():
        popup_html = '<b>' + row['Name'] + '</b><br>' + row['Address']
        marker = folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup_html)
        marker.add_to(map)

    st.components.v1.html(map._repr_html_(), width=700, height=500)


st.title("GetHigh🍻")


if st.button("HOME"):
    home()

st.text("")


if st.button("PUBS"):
    pubs()

st.text("")

if st.button("Find Pubs "):
    findpubs()
