
# from machine import SoftI2C, Pin
# from time import sleep
# from ADS1115 import *

# ADS1115_ADDRESS = 72
# i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
# 
# adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)
# adc.setVoltageRange_mV(ADS1115_RANGE_6144)
# adc.setCompareChannels(ADS1115_COMP_0_GND)
# adc.setMeasureMode(ADS1115_SINGLE)
# 
# def readChannel(channel):
#     adc.setCompareChannels(channel)
#     adc.startSingleMeasurement()
#     while adc.isBusy():
#         pass
#     voltage = adc.getResult_V()
#     return voltage
# 
# 
# while True:
#     voltage = readChannel(ADS1115_COMP_0_GND)
#     value = ((65536/3.3)*voltage)
#     value_min = 0
#     if value < 0:
#         value = value_min
#     value_percent = (value/65536)*100
#     print("Value: %5.2f" % (value_percent), "%")
# 
#     sleep(0.2)

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
