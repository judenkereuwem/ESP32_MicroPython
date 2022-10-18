from time import sleep
from machine import Pin
from machine import PWM

pwm = PWM(Pin(2))
pwm.freq(50)

def setServoCycle(position):
    pwm.duty_u16(position)
    sleep(0.01)
    
def angle(ang):
    deg = ang * 50
    return deg

init_pos = angle(0)
final_pos = angle(90)

for pos in range(init_pos, final_pos, 30):
    setServoCycle(pos)

# while True:
#     for pos in range(init_pos, final_pos, 30):
#         setServoCycle(pos)
#     for pos in range(final_pos, init_pos, -30):
#         setServoCycle(pos)
        
#     for pos in range(4500, 1000, -20):
#         setServoCycle(pos)
    
    