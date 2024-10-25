import requests
import wifi_config

IP_ADDRESS = wifi_config.IP_ADDRESS

ENDPOINTS = {
    'Test': 'test', 
    'GET': 'get_feed',
    'DELETE': 'delete_feed'
}

class Bridge:
    def __init__(self):
        pass

    def get_schedule(self, endpoint):

        if endpoint not in ENDPOINTS:
            raise RuntimeError('Endpoint not defined!')

        url = f"http://{IP_ADDRESS}/api/{ENDPOINTS[endpoint]}"
        response = requests.get(url)

        print('Response Code:', response.status_code)
        data = response.json()

        response.close()

        for item in data:
            self.feed_id = item["id"]
            self.created_at = item["created_at"]
            self.updated_at = item["updated_at"]
            self.deleted_at = item["deleted_at"]
            self.pet_name = item["Pet_Name"]
            self.date_to_feed = item["Date_to_Feed"]
            self.feed_time = item["Feed_Time"]
            self.feeding_amount = item["Feeding_Amount"]

    def update_schedule(self):
        return 1 # TODO return the next feed time by querying the web app translate the date and time into seconds and return

    def delete_feed(self):
        pass