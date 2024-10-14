from machine import Pin

class PicoPins:
    def __init__(self):
        self.led = Pin(25, Pin.OUT)

    def blink(self):
        self.led.toggle()



    def dispense_food(self):
        pass


    def weigh_food(self):
        pass


    