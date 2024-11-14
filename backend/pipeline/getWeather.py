#pip install pyown

from dotenv import load_dotenv
load_dotenv(override=True)

import os

from langchain_community.utilities import OpenWeatherMapAPIWrapper

weather = OpenWeatherMapAPIWrapper()

weather_data = weather.run("Malaysia, MY")
print(weather_data)


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM(os.getenv("OPENWEATHERMAP_API_KEY"))
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('Malaysia, MY')
w = observation.weather

print(w.detailed_status)
print(w.wind())
print(w.humidity)
print(w.temperature('celsius'))
print(w.rain)
print(w.heat_index)
print(w.clouds)