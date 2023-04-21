import streamlit as st
import pandas as pd
import folium
import math

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
