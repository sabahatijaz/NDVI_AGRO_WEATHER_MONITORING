import pyowm
owm = pyowm.OWM('API_Key')
mgr = owm.agro_manager()
# first create the pyowm.utils.geo.Polygon instance that represents the area (here, a triangle)
from pyowm.utils.geo import Polygon as GeoPolygon
gp = GeoPolygon([[
        [-121.1958, 37.6683],
        [-121.1779, 37.6687],
        [-121.1773, 37.6792],
        [-121.1958, 37.6683]]])

# use the Agro Manager to create your polygon on the Agro API
# the_new_polygon = mgr.create_polygon(gp, 'my new shiny polygon')
the_new_polygon=mgr.get_polygon("Ploygon_ID")
# the new polygon has an ID and a user_id
print(the_new_polygon.id)
print(the_new_polygon.user_id)
soil = mgr.soil_data(the_new_polygon)
print(soil)
print(soil.polygon_id)                     # str
print(soil.reference_time(timeformat='unix'))  # can be: int for UTC Unix time ('unix'),
                                        # ISO8601-formatted str for 'iso' or
                                        # datetime.datetime for 'date'
print(soil.surface_temp(unit='kelvin'))        # float (unit can be: 'kelvin', 'celsius' or 'fahrenheit')
print(soil.ten_cm_temp(unit='kelvin'))       # float (Kelvins, measured at 10 cm depth) - unit same as for above
print(soil.moisture)






from pyowm.commons.enums import ImageTypeEnum
from pyowm.agroapi10.enums import SatelliteEnum, PresetEnum

pol_id = str(the_new_polygon.id)  # your polygon's ID
acq_from = 1500336000                # 18 July 2017
acq_to = 1508976000                  # 26 October 2017
img_type = ImageTypeEnum.PNG     # the image format type
preset = PresetEnum.NDVI    # the preset
sat = SatelliteEnum.SENTINEL_2.symbol # the satellite


# the search returns images metadata (in the form of `MetaImage` objects)
results = mgr.search_satellite_imagery(polygon_id=pol_id, acquired_from=acq_from, acquired_to=acq_to, img_type=img_type, preset=preset,acquired_by=sat)

# download all of the images
satellite_images = [mgr.download_satellite_image(result) for result in results]

# get stats for the first image
sat_img = satellite_images[0]
stats_dict = mgr.stats_for_satellite_image(sat_img)

# ...satellite images can be saved to disk
sat_img.persist('/path/to/my/folder/sat_img.png')