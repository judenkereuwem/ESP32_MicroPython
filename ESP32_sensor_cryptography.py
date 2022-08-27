#read, encrypt and decrypt esp32 sensor data with microPython


from machine import ADC, Pin
import time
import uos
from ucryptolib import aes
import ucryptolib

adc = ADC(Pin(4))

MODE_CBC = 2

BLOCK_SIZE = 16
 
key = b'I_am_32bytes=256bits_key_padding'

while True:
    
    data = str(adc.read_u16())
    print('\nRaw Data:', data)

    # Padding plain text with space 
    pad = BLOCK_SIZE - len(data) % BLOCK_SIZE
    data = data + " "*pad
     
    # Generate iv with HW random generator 
    iv = uos.urandom(BLOCK_SIZE)
    cipher = aes(key,MODE_CBC,iv)
     
    encrypted = iv + cipher.encrypt(data)
    print ('Encrypted Data:', encrypted)
     
    iv = encrypted[:BLOCK_SIZE]
    cipher = aes(key,MODE_CBC,iv)
    decrypted = cipher.decrypt(encrypted)[BLOCK_SIZE:]
    print('Decrypted Data:', decrypted)
    
    time.sleep(2)
