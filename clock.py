import utime
import ntptime

class Clock:
    def __init__(self):
        self.current_datetime = utime.localtime()
        ntptime.settime()
        self.year, self.month, self.day, self.hour, self.minute, self.second, _, _ = self.current_datetime

    def current_clock(self, param):
        if param == 'date':
            return f"{self.year}-{self.month}-{self.day}"
        elif param == 'time':
            return  f"{self.hour}:{self.minute}:{self.second}"