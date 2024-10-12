import network 
import time
from dotenv import load_dotenv
import os

load_dotenv()

SSID = os.getenv('SSID')
PASSWORD = os.getenv('PASSWORD')

class WIFI_CONNECTION(): 
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.initialise_wifi()

    def initialise_wifi(self):
        self.wlan.active(True)
        self.wlan.connect(SSID, PASSWORD)

    def connect_to_wifi(self):
        CONNECTION_TIMEOUT = 10
        while CONNECTION_TIMEOUT >0:

            status = self.wlan.status()
            config = self.wlan.ifconfig()

            if status >=3:
                break

            else:
                CONNECTION_TIMEOUT -=1
                print('Waiting for Wifi Connection')
                time.sleep(1)

        if status !=3:
            raise RuntimeError('Failed to Make a Connection!')

        else:
            print(f"Connection Established! {config[0]}")       


