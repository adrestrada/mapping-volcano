#!/usr/bin/env python
# coding: utf-8

# <h1 style="font-size:2rem;color:blue;">1)</h1>

# In[10]:


get_ipython().run_line_magic('pip', 'install folium')


# In[2]:


#import folium
# if you can't import folium package, try this in a individual cell (%pip install folium)
import pandas as pd
#read
data = pd.read_csv('C:/Users/Valeria/Desktop/Volcanoes.txt')
#creo lista 
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


# In[3]:


#defino mi funcion 'color_producer' y un bloque de instrucciones
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [43.642, -79.387], zoom_start = 4, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el, nme in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location = [lt, ln], radius = 7, popup = nme, 
    fill_color = color_producer(el), color = 'grey', fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("MainMap.html")


# In[ ]:




