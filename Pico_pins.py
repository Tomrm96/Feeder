from machine import Pin, PWM
import time

class PicoPins:
    def __init__(self):
        self.led = Pin(25, Pin.OUT)
        self.servo_pin = PWM(Pin(16))
        self.servo_pin.freq(50)

        self.max_duty = 7864
        self.min_duty = 1802
        self.half_duty = int(self.max_duty /2)

    def blink(self):
        self.led.toggle()



    def dispense_food(self):
        pass


    def weigh_food(self):
        pass


    def servo_test(self):

        self.servo_pin.duty_u16(self.min_duty)
        time.sleep(2)
        
        self.servo_pin.duty_u16(self.half_duty)
        time.sleep(2)

        self.servo_pin.duty_u16(self.max_duty)
        time.sleep(2)    

        self.servo_pin.deinit()
      