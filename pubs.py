import pandas as pd
import folium
from geopy.geocoders import Nominatim
import streamlit as st


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
