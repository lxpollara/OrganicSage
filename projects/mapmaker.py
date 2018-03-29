import folium
map_osm = folium.Map(location=[42.396282, -83.245248],zoom_start=5)
map_osm.save('/home/PycharmProjects/OrganicSage/templates/map.html')
