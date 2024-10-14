import requests
import wifi_config

API_KEY = wifi_config.WEATHER_API_KEY
location = 'Warrington'

url = f"https://api.weatherapi.com/v1/current.json?q={location}+&key={API_KEY}"

class Bridge:
    def __init__(self):
        pass

    def get_schedule(self):
        pass

    def update_schedule(self):
        pass

    def get_test(self):

        response = requests.get(url)
        print('Response Code:', response.status_code)
        weather = response.json()
        response.close()

        print(weather)