from machine import Pin, PWM
import time

class PicoPins:
    def __init__(self):
        self.led = Pin(25, Pin.OUT)
        self.servo_pin = PWM(Pin(16))
        self.servo_pin.freq(50)
        self.backwards_value = 6553   
        self.forward_value = 3276   
        self.stop_value = 4915  

    def blink(self):
        self.led.toggle()

    def servo_forward(self, amount):
        for i in range(0, amount):
            self.servo_pin.duty_u16(self.forward_value)
            time.sleep(0.6)
            self.servo_pin.duty_u16(self.stop_value)
            time.sleep(1)
        self.servo_pin.deinit()
      
    def servo_backward(self, amount):
        for i in range(0, amount):
            self.servo_pin.duty_u16(self.backwards_value)
            time.sleep(0.6)
            self.servo_pin.duty_u16(self.stop_value)
            time.sleep(1)
        self.servo_pin.deinit()
        
    def dispense_food(self):
        pass

    def weigh_food(self):
        pass
