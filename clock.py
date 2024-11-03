import utime
import ntptime
import time
from Pico_pins import PicoPins

class Clock:
    def __init__(self):
        self.update_clock()
        self.pins = PicoPins()

    def update_clock(self):
        ntptime.host = "ntp1.npl.co.uk"
        ntptime.settime()
        time.sleep(0.5)
        self.current_datetime = utime.localtime()
        time.sleep(0.5)
        self.hour, self.minute = f"{self.current_datetime[3] +1 :02d}", f"{self.current_datetime[4]:02d}"
        self.year, self.month, self.day, _, _, self.seconds, _, _ = self.current_datetime

    def current_clock(self, param):
        self.update_clock()
        if param == 'date':
            date =  f"{self.year}-{self.month}-{self.day}"
            return date
        elif param == 'time':
            time = f"{self.hour}:{self.minute}"
            return time
        elif param == 'last_feed_time':
            time = f"{self.hour}:{self.minute}:{self.seconds}"
            return time