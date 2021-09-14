from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.weatherapi25.forecast import Forecast
# Forecast('3h',)

# ---------- FREE API KEY examples ---------------------

owm = OWM('API_KEY')
mgr = owm.weather_manager()
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Lahore,PK')
w = observation.weather
print("###################################################################")
print("Detailed Status")
print(w.detailed_status)         # 'clouds'
print("###################################################################")

print("###################################################################")
print("Wind")
print(w.wind())             # {'speed': 4.6, 'deg': 330}
print("###################################################################")

print("###################################################################")
print("Humidity")
print(w.humidity)                # 87
print("###################################################################")

print("###################################################################")
print("Temperature Celsius")
print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print("###################################################################")

print("###################################################################")
print("Rain")
print(w.rain)                    # {}
print("###################################################################")

print("###################################################################")
print("HeatIndex")
print(w.heat_index)              # None
print("###################################################################")

print("###################################################################")
print("Clouds")
print(w.clouds)                  # 75
print("###################################################################")


# Will it be clear tomorrow at this time in Milan (Italy) ?
forecast = mgr.forecast_at_place('Milan,IT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())
print("###################################################################")
print("Will it be clear tomorrow at this time in Milan (Italy) ?")
print(answer)
print("###################################################################")


# ---------- PAID API KEY example ---------------------

config_dict = config.get_default_config_for_subscription_type('professional')
owm = OWM('API_KEY', config_dict)

# What's the current humidity in Berlin (Germany) ?
one_call_object = mgr.one_call(lat=52.5244, lon=13.4105)
print("###################################################################")
print(one_call_object.current.humidity)
print("###################################################################")
