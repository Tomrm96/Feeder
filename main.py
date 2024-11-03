from wifi import WIFI_CONNECTION
from bridge import Bridge
from Pico_pins import PicoPins
from clock import Clock
from dispense_food import Dispense
import time

wifi = WIFI_CONNECTION()
get_schedule = Bridge()
pico_pins = PicoPins()
clock = Clock()
dispenser = Dispense()

# Error Blinks:

# Two Blinks = Couldn't connect to WIFI
# Three Blinks = 

# Normal Blinks:
# One Blink = Looking for WIFI
# Five Blinks = Connected to WIFI
# Four Blinks = Recieved JSON Payload
# Ten Blinks = Dispensing food

while True:
    
    time.sleep(5)

    get_schedule.get_schedule('GET')    

    next_feed = get_schedule.update_schedule() 
    print()

    if get_schedule.date_to_feed == clock.current_clock('date') and get_schedule.feed_time == clock.current_clock('time'):
        dispenser.dispense(get_schedule.feeding_amount)
        time.sleep(70)

    # wifi.disconnect_wifi()

    time.sleep(next_feed - 60) 

# TODO Find if there is a row after the current row, if there is set the sleep time for the 
# time until the next row minus 60 seconds for a buffer. If no row, set the sleep to 10 seconds so it checks for new feeds. 

# TODO Think of a way of sending an update to the PICO so we can send manual feeds, otherwise it wont pick up feeds until the next scheduled feed.

# TODO Send a Put request to the API to soft delete the current feed in the database indicating its been carried out.

# TODO Show that the feed has been executed on the web GUI by checking if its been soft deleted, if it has make the record green. 