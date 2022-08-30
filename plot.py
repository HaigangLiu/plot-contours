import geopandas as gpd
from folium import GeoJson
import folium

SHELBY_COUNTY_CODE = '157'  ## it's 47 157
TN_CODE = '47'
geo_file_memphis = gpd.read_file('cb_2018_us_county_5m/cb_2018_us_county_5m.shp')
geom = geo_file_memphis[(geo_file_memphis['COUNTYFP'] == SHELBY_COUNTY_CODE) & (geo_file_memphis['STATEFP'] == TN_CODE)]
geom = geom['geometry']
geo_file_tn = gpd.read_file('https://raw.githubusercontent.com/johan/world.geo.json/master/countries/USA/TN.geo.json')

# initiate a canvas
map_object = folium.Map(location=[35.644800, -86.216721], zoom_start=6)

# add markers and countours
folium.Marker(location=[35, -85], popup='<h3 style="color:green;">Your house</h3>',
              tooltip='<strong>1732 hunter bluff</strong>').add_to(map_object)
GeoJson(geom, style_function=lambda feature: {
    'fillColor': 'red',
    'weight': 1,
    'fillOpacity': 0.5,
}).add_to(map_object)
GeoJson(geo_file_tn).add_to(map_object)

# show the map
map_object.save('test_file.html')
