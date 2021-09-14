import pyowm

owm = pyowm.OWM('Your API Key')
mgr = owm.agro_manager()
# first create the pyowm.utils.geo.Polygon instance that represents the area (here, a triangle)
from pyowm.utils.geo import Polygon as GeoPolygon

gp = GeoPolygon([[
    [31.51494213249819, 74.32886335947272],
    [31.514064076457466, 74.33564398375346],
    [31.510734705687554, 74.33701727474703],
    [31.50952732214692, 74.33032248115337],
           [31.51494213249819, 74.32886335947272]]])

# # use the Agro Manager to create your polygon on the Agro API
the_new_polygon = mgr.create_polygon(gp, 'my new shiny polygon')
mgr.update_polygon()
import requests

startdate = 1625042736
enddate = 1630313136
polId = 'Pol_ID'
ApID = 'API_Key'

response = requests.get(
    f'http://api.agromonitoring.com/agro/1.0/image/search?start={startdate}&end={enddate}&polyid={the_new_polygon.id}&appid={ApID}')
# print(response.json())
response = response.json()
print(response)
# print(response.text)
# print(type(response))
# response1=requests.get(f'http://api.agromonitoring.com/agro/1.0/image/search?start={startdate}&end={enddate}&polyid={polId}&appid={ApID}')
print(response[0]['image']['ndvi'])
img1 = response[0]['image']['ndvi']
response1 = requests.get(img1)
file = open("sample_image4.png", "wb")
file.write(response1.content)
file.close()
