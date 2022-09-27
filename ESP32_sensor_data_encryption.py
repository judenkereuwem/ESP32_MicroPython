#read, encrypt and decrypt esp32 sensor data with microPython

from machine import ADC, Pin
import time
import uos
from ucryptolib import aes
import ucryptolib
from machine import SoftI2C, Pin
from ADS1115 import *

#print(i2c.scan())
ADS1115_ADDRESS = 72
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)

adc = ADS1115(ADS1115_ADDRESS, i2c=i2c)
adc.setVoltageRange_mV(ADS1115_RANGE_6144)
adc.setCompareChannels(ADS1115_COMP_0_GND)
adc.setMeasureMode(ADS1115_SINGLE)

MODE_CBC = 2
BLOCK_SIZE = 16
 
key = b'I_am_32bytes=256bits_key_padding'

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

    data = str("%5.2f" % (value_percent))
    print("\nOriginal Data:  ", data)

    # Padding plain text with space 
    pad = BLOCK_SIZE - len(data) % BLOCK_SIZE
    data = data + " "*pad
     
    # Encryption
    iv = uos.urandom(BLOCK_SIZE)
    cipher = aes(key,MODE_CBC,iv)
    encrypted = iv + cipher.encrypt(data)
    print ('Encrypted Data: ', encrypted)
     
    # Decryption 
    iv = encrypted[:BLOCK_SIZE]
    cipher = aes(key,MODE_CBC,iv)
    decrypted = cipher.decrypt(encrypted)[BLOCK_SIZE:]
    print('Decrypted Data: ', decrypted.decode('utf-8'))
    
    time.sleep(1)
