import folium
import pandas

data=pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
ele=list(data["ELEV"])

def colormaker(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation<3000:
        return 'yellow'
    else:
        return 'red'

map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
fgv=folium.FeatureGroup(name="Volcanoes")
fgp=folium.FeatureGroup(name="Population")

for i,j,k in zip(lat,lon,ele):
    fgv.add_child(folium.CircleMarker(location=[i,j],radius=6,popup=str(k)+" m",fill_color=colormaker(k),color='grey',fill_opacity=0.7))

fgp.add_child(folium.GeoJson(data=(open('world.json','r',encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<1000000 else 'orange' if 1000000<=x['properties']['POP2005']<2000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map.html")