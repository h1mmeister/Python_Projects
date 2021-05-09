from folium import Map

latitude = 40.09
longitude = -3.47

# dir(int) and dir(__builtins__)
antipode_latitude = latitude * (-1)

if longitude <= 0:
    antipode_longitude = longitude + 180
else:
    antipode_longitude = longitude - 180

location = [antipode_latitude, antipode_longitude]

world_map = Map(location)
world_map.save("map.html")

print(antipode_latitude)
print(antipode_longitude)
