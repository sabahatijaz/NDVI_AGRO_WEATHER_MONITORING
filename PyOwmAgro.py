import pyowm
from pyowm.commons.enums import ImageTypeEnum
from pyowm.agroapi10.enums import SatelliteEnum, PresetEnum, PaletteEnum

owm = pyowm.OWM('API_Key')
mgr = owm.agro_manager()
# first create the pyowm.utils.geo.Polygon instance that represents the area (here, a triangle)
from pyowm.utils.geo import Polygon as GeoPolygon
# gp = GeoPolygon([[
#         [-121.1958, 37.6683],
#         [-121.1779, 37.6687],
#         [-121.1773, 37.6792],
#         [-121.1958, 37.6683]]])
#
# # use the Agro Manager to create your polygon on the Agro API
# the_new_polygon = mgr.create_polygon(gp, 'my new shiny polygon')
the_new_polygon=mgr.get_polygon('Pol_id')
# mgr.delete_polygon(the_new_polygon)
# the new polygon has an ID and a user_id
print(the_new_polygon.id)
print(the_new_polygon.user_id)
# my_polygon.name  # "my new shiny polygon"
the_new_polygon.name = "changed name"
mgr.update_polygon(the_new_polygon)

soil = mgr.soil_data(the_new_polygon)
print(soil.polygon_id)                         # str
print(soil.reference_time(timeformat='unix'))  # can be: int for UTC Unix time ('unix'),
                                        # ISO8601-formatted str for 'iso' or
                                        # datetime.datetime for 'date'
print(soil.surface_temp(unit='kelvin'))        # float (unit can be: 'kelvin', 'celsius' or 'fahrenheit')
print(soil.ten_cm_temp(unit='kelvin'))         # float (Kelvins, measured at 10 cm depth) - unit same as for above
print(soil.moisture)                           # float (m^3/m^3)

acq_from = 1625042736              # 18 July 2017
acq_to = 1630313136                  # 26 October 2017
img_type = ImageTypeEnum.GEOTIFF     # the image format type
preset = PresetEnum.NDVI    # the preset
sat = SatelliteEnum.SENTINEL_2.symbol # the satellite


# the search returns images metadata (in the form of `MetaImage` objects)
results = mgr.search_satellite_imagery(the_new_polygon.id, acq_from, acq_to, img_type=img_type, preset=preset, acquired_by=sat)
print(results)
# print(len(results))
# print(results[0])
# mgr.download_satellite_image(results[0])
# download all of the images
try:
    satellite_images = [mgr.download_satellite_image(result) for result in results]
except Exception as e:
    raise e
# print(len(satellite_images))
# # get stats for the first image
# sat_img = satellite_images[0]
# stats_dict = mgr.stats_for_satellite_image(sat_img)

# ...satellite images can be saved to disk
# sat_img.persist('sat_img.tif')