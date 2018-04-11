import folium
import os


def map_gen(projects):
    map_osm = folium.Map(location=[0, 0], zoom_start=2.1, tiles='cartodbpositron')

    for location in projects:
        if location.type == 'Consulting':
            color = '#f9d908'
        elif location.type == 'Inspection':
            color = '#67aeff'
        else:
            color = '#0d0b16'

        popup = folium.Popup('<a href= "/blog/post/{}", target="_parent" > {} </a>'.format(location.blog_post, location.name), max_width=2650)
        folium.RegularPolygonMarker([location.latitude, location.longitude], popup=popup, color=color, fill_color=color, radius=5).add_to(map_osm)
    # TODO got to figure out how best to manage directories on the bitnami distro current solution is hacky cancer
    map_osm.save(os.path.join(os.path.abspath(''), 'templates/map.html'))
