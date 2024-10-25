import requests
import wifi_config

IP_ADDRESS = wifi_config.IP_ADDRESS

url = f"http://{IP_ADDRESS}/api/test"

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
        data = response.json()
        response.close()

        for item in data:
            for key, value in item.items():
                print(f"{key}: {value}")
