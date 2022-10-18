
from machine import SoftI2C, Pin
from time import sleep
from ADS1115 import *

ADS1115_ADDRESS = 72
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)
adc.setVoltageRange_mV(ADS1115_RANGE_6144)
adc.setCompareChannels(ADS1115_COMP_0_GND)
adc.setMeasureMode(ADS1115_SINGLE)

def readChannel(channel):
    adc.setCompareChannels(channel)
    adc.startSingleMeasurement()
    while adc.isBusy():
        pass
    voltage = adc.getResult_V()
    return voltage


while True:
    voltage = readChannel(ADS1115_COMP_0_GND)
    value = ((65536/3.3)*voltage)
    value_min = 0
    if value < 0:
        value = value_min
    value_percent = (value/65536)*100
    print("Value: %5.2f" % (value_percent), "%")

    sleep(0.2)


