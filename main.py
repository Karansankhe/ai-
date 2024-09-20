
import streamlit as st
from streamlit_folium import st_folium
import folium

# Set page title
st.set_page_config(page_title="India Map with Locations", page_icon="🗺️")

# Create a map centered on India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Hardcode some locations (latitude and longitude) in India
locations = [
    {"name": "New Delhi", "coords": [28.6139, 77.2090]},
    {"name": "Mumbai", "coords": [19.0760, 72.8777]},
    {"name": "Chennai", "coords": [13.0827, 80.2707]},
    {"name": "Kolkata", "coords": [22.5726, 88.3639]},
    {"name": "Bangalore", "coords": [12.9716, 77.5946]},
]

# Add markers for each location
for location in locations:
    folium.Marker(
        location=location["coords"],
        popup=location["name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(india_map)

# Display the map in Streamlit
st.markdown("<h1 style='text-align: center;'>India Map with Key Locations</h1>", unsafe_allow_html=True)
st.write("Below is a map of India with some key cities marked:")

# Render the map in Streamlit using streamlit_folium
st_folium(india_map, width=725)

# Footer
st.write("Powered by Streamlit and Folium.")
