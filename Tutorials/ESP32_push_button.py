from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN)

while True:
    button_state = button.value()
    if button_state == True:
        led.value(1)
        print("led on")   
    else:
        led.value(0)
        print("led off")
        
    sleep(0.1)