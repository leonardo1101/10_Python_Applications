import folium
import pandas


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 3000:
        return "orange"
    else:
        return "red"

if __name__ == "__main__":
    data = pandas.read_csv("data/Volcanoes.txt")
    lon = list(data["LON"])
    lat = list(data["LAT"])
    names = list(data["NAME"])
    elev = list(data["ELEV"])

    map = folium.Map(location=[39.383567, -104.513780], zoom_start=3,
            titles="Stamen Terrain")
    fgv = folium.FeatureGroup(name="Volcanoes")
    fgp = folium.FeatureGroup(name="Population")

    # Volcanoes  markers creation
    for lt, ln, name, elv in zip(lat, lon, names, elev):
        fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=8,
                popup="Name: %s Elevation: %.2fm" % (name, elv),
                fill_color=color_producer(elv), color="grey", fill_opacity=0.7))

    # Population density 
    fgp.add_child(folium.GeoJson(data=open("data/world.json", "r",
            encoding="utf-8-sig").read(),
            style_function=lambda x:
            {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
            else 'orange' if x['properties']['POP2005'] < 20000000
            else 'red '}))

    map.add_child(fgv)
    map.add_child(fgp)
    map.add_child(folium.LayerControl())
    map.save("Map1.html")
