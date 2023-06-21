
import utime
from machine import I2C, Pin
 
dev = I2C(1, freq=400000, scl=Pin(22), sda=Pin(21))
devices = dev.scan()
for device in devices: print(device)
address = 72
 
def read_config():
    dev.writeto(address, bytearray([1]))
    result = dev.readfrom(address, 2)
    return result[0] << 8 | result[1]
 
def read_value():
    dev.writeto(address, bytearray([0]))
    result = dev.readfrom(address, 2)
    config = read_config()
    config &= ~(7 << 12) & ~(7 << 9)
    config |= (4 << 12) | (1 << 9) | (1 << 15)
    config = [int(config >> i & 0xff) for i in (8, 0)]
    dev.writeto(address, bytearray([1] + config))
    return result[0] << 8 | result[1]
 
def val_to_voltage(val, max_val=26100, voltage_ref=3.3):
    return val / max_val * voltage_ref
 
print(bin(read_config()))
 
while True:
    val = read_value()
    voltage = val_to_voltage(val)
    print("ADC Value:", val, "Voltage: {:.3f} V".format(voltage))
    utime.sleep(0.5)
