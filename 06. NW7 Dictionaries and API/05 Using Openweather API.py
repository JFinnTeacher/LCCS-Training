from pyowm.owm import OWM

# defining your personal API key obtained from openweathermap.org
my_api_key = '7cfa293351042a6fa3696d66a3a96983'

# linking your api key with the python to talk to OWM
owm = OWM(my_api_key)
mgr = owm.weather_manager()

# calling the API for weather data at your preferred location
obvs = mgr.weather_at_place('Portmagee,IE').weather
#print(obvs)

wind_dict = obvs.wind()
print(wind_dict)
rain_dict = obvs.rain
print(rain_dict)
temperature_dict = obvs.temperature('celsius')

Portmagee = {}
print(Portmagee)
Portmagee['Temperature']=temperature_dict['feels_like']
print(Portmagee)


Portmagee['Wind'] = wind_dict['speed']
print(Portmagee)


allWeather = {}
allWeather['Portmagee'] = Portmagee
print(allWeather)
