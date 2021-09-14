import pyowm
import time
import pyowm
from matplotlib.pyplot import arrow
from pyowm.commons.exceptions import APIResponseError
import urllib3
from colorama import *
from pyowm.commons.exceptions import *
from pyowm.utils.geo import Polygon as GeoPolygon

gp = GeoPolygon([[
        [-121.1958, 37.6683],
        [-121.1779, 37.6687],
        [-121.1773, 37.6792],
        [-121.1958, 37.6683]]])
def weather():
    # create OWM object
    API_key = 'API+KEY'
    owm = pyowm.OWM(API_key)


    theCity = "Seattle"
    theState = "WA"
    weatherCityState = theCity + ", " + theState
    weatherLocation = theCity + ",US"

    # get currently observed weather for Seattle, WA, US
    obs = owm.weather_manager().weather_at_place(weatherLocation)
    # agromgr=owm.agro_manager()
    # poly=agromgr.create_polygon(gp)
    # agromgr.download_satellite_image()
    w=obs.weather
    print(w)
    s=w.get_detailed_status
    # get weather object for current Seattle weather
    # w = obs.get_weather()
    print(w)
    print(s)

    # get current weather status and temperature in fahrenheit
    currStatus = w.get_detailed_status()
    tempF = w.get_temperature('fahrenheit')["temp"]

    # query the daily forcast for Seattle, WA, US, for the next 5 days
    fc = owm.daily_forecast('Seattle,US', limit=5)

    # get a forcaster object
    f = fc.get_forecast()

    return render_template('templateWeather.html', theLocation=weatherCityState, currStatus=currStatus, theTemp=tempF, forecast=f,
                           title="Weather", arrow=arrow)
if __name__ == '__main__':
    weather()