from pyowm.owm import OWM

# defining your personal API key obtained from openweathermap.org
my_api_key = '7cfa293351042a6fa3696d66a3a96983'

# linking your api key with the python to talk to OWM
owm = OWM(my_api_key)
mgr = owm.weather_manager()
places_wind = {}
towns = ['Killybegs, IE', 'Belmullet, IE', 'Clifden, IE', 'Doolin, IE', 'Kilkee, IE', 'Ventry, IE','Portmagee, IE','Bantry, IE','Baltimore, IE']
for item in towns:
    observation = mgr.weather_at_place(item).weather
    wind_dictionary = observation.wind()
    places_wind[item] = wind_dictionary["speed"]
print("Dictionary with places:temperature keys: ",places_wind)
fastest = max(places_wind, key = places_wind.get)
print (fastest)