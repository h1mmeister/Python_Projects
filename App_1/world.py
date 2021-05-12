from folium import Map
from geo import Geopoint

# Get Latitude and Longitude values
latitude = 40.09
longitude = -3.47

antipode_latitude = latitude * (-1)

if longitude <= 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180

location = [antipode_latitude, antipode_longitude]

world_map = Map(location)
world_map.save("map.html")

my_point = Geopoint(antipode_latitude, antipode_longitude)
print(my_point.closest_parallel())

print(antipode_latitude)
print(antipode_longitude)

# dir(int) to see all the methods and dir(__builtins__) to see all builtins functions