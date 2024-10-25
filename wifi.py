import network 
import time
import wifi_config
from Pico_pins import PicoPins

STATUS_CODES = {
    0: 'WLAN is not enabled.', 
    1: 'Currently scanning for networks.', 
    2: 'Connecting to a network..', 
    3: 'Connected to a network!', 
    4: 'Failed to connect to a network!', 
}

class WIFI_CONNECTION(): 
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.pins = PicoPins()
        self.available_networks =[]
        self.wlan.active(True)
        self.connect_to_wifi()

    def scan_for_wifi(self):
        self.available_SSIDS = self.wlan.scan()
        for SSID in self.available_SSIDS:
            decoded = SSID[0].decode('utf-8')
            self.available_networks.append(decoded)

    def initialise_wifi(self):
        self.scan_for_wifi()

        for ssid in wifi_config.NETWORKS.keys():
                if ssid in self.available_networks:
                    self.wlan.connect(ssid, wifi_config.NETWORKS[ssid]['password'])
                    break
        else:
            raise RuntimeError('Known Networks Out Of Range!')

    def connect_to_wifi(self):

        self.initialise_wifi()

        CONNECTION_TIMEOUT = 10

        while CONNECTION_TIMEOUT >0:

            self.pins.blink()
            
            status = self.wlan.status()
            config = self.wlan.ifconfig()

            if status >=3:        
                break
            
            elif status ==0:
                raise RuntimeError('WLAN Is Not Turned On!')

            else:
                CONNECTION_TIMEOUT -=1
                print('Waiting for Wifi Connection')
                print(STATUS_CODES[status])
                time.sleep(1)

        if status !=3:
            raise RuntimeError('Failed to Make a Connection!')

        else:
            print(f"{STATUS_CODES[status]} Your IP Address is: {config[0]}")       
        
    def disconnect_wifi(self):
        self.wlan.disconnect()
        print('Wifi Disconnected!')