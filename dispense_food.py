from Pico_pins import PicoPins

class Dispense:
    def __init__(self):
        self.pico_pins = PicoPins()

    def dispense(self, turns):
        self.pico_pins.servo_forward(turns)