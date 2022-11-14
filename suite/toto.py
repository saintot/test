import time
from machine import Pin
led = Pin(2, Pin.OUT)

for i in range (110):
     led.off()
     time.sleep(1)
     led.on()
     time.sleep(1)
