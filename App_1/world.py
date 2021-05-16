from folium import Map, Marker, Popup
from geo import Geopoint

# Get Latitude and Longitude values
latitude = 40.4
longitude = -3.7

# Folium Map Instance
world_map = Map(location = [latitude, longitude])

# Create a Geopoint instance
geo_point = Geopoint(latitude = latitude, longitude = longitude)
popup = Popup(str(geo_point.get_weather()))
popup.add_to(geo_point)
geo_point.add_to(world_map)

# Create a marker instance and add to map
# madrid = Marker(location = [latitude, longitude], popup = "Madrid")
# madrid.add_to(world_map)

# Save the map instance into an HTML file
world_map.save("map.html")

# dir(int) to see all the methods and dir(__builtins__) to see all builtins functions