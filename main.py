from wifi import WIFI_CONNECTION
from bridge import Bridge
from Pico_pins import PicoPins
import time


wifi = WIFI_CONNECTION()
get_schedule = Bridge()
pico_pins = PicoPins()


loop = 1

while loop > 0:

    print(loop)

    wifi.connect_to_wifi()

    time.sleep(3) 

    pico_pins.servo_forward(1)

    time.sleep(1)

    pico_pins.servo_backward(1)

    get_schedule.get_test()

    wifi.disconnect_wifi()

    loop -=1
# Check the Web app to look for updates to schedules


# if update, update the current schedule dictionary. 



# if there is a feed scheduled, execute the feeder

