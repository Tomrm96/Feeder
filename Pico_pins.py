from machine import Pin, PWM
import time

class PicoPins:
    def __init__(self):
        self.led = Pin('LED', Pin.OUT)
        self.servo_pin = PWM(Pin(16))
        self.servo_pin.freq(50)
        self.backwards_value = 6553   
        self.forward_value = 3276   
        self.stop_value = 4915  

    def blink(self, num):
        for i in range(0,num):
            self.led.value(True)
            time.sleep(0.2)
            self.led.value(False)
            time.sleep(0.2)
        self.led.value(False)

    def error_blink(self, num):
        for i in range(0,num):
            self.led.value(True)
            time.sleep(0.5)
            self.led.value(False)
            time.sleep(0.5)
        self.led.value(False)

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
        
    def weigh_food(self):
        pass
