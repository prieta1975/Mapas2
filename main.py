from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=-10.5,llcrnrlat=33,urcrnrlon=10,urcrnrlat=46, epsg=5520)
#http://server.arcgisonline.com/arcgis/rest/services

map.arcgisimage(service='ESRI_StreetMap_World_2D', xpixels = 1500, verbose= True)

x, y = map(-3.7037901999999576, 40.4167754)  # Obtiene las coordenadas de Madrid para dibujar a partir de latitud y longitud
map.plot(x, y, 'bo', markersize = 10)

plt.show()

