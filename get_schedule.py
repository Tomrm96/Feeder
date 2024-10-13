import requests

class GetSchedule:
    def __init__(self):
        pass

    def get_test(self):

        response = requests.get("http://www.google.com")

        response_code = response.status_code

        print('Response code: ', response_code)
