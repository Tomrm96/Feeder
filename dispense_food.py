from Pico_pins import PicoPins

class Dispense:
    def __init__(self):
        self.pico_pins = PicoPins()

    def dispense(self, turns):
        self.notify(turns)
        self.pico_pins.servo_forward(turns)
        
    def notify(self, turns):
        for i in range(0, 10):
            self.pico_pins.blink(1) 