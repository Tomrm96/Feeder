from wifi import WIFI_CONNECTION
from bridge import Bridge


wifi = WIFI_CONNECTION()
get_schedule = Bridge()


# Connect to WIFI

wifi.connect_to_wifi()

get_schedule.get_test()

wifi.disconnect_wifi()


# Check the Web app to look for updates to schedules


# if update, update the current schedule dictionary. 



# if there is a feed scheduled, execute the feeder
