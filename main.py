from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=3.75,llcrnrlat=39.75,urcrnrlon=4.35,urcrnrlat=40.15, epsg=5520)
#http://server.arcgisonline.com/arcgis/rest/services

map.arcgisimage(service='ESRI_StreetMap_World_2D', xpixels = 1500, verbose= True)

x, y = map(3.8, 40)  # Obtiene las coordenadas para dibujar a partir de latitud y longitud
map.plot(x, y, 'bo', markersize = 24)

plt.show()