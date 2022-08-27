#Encrypt data with CTR

import uos
from ucryptolib import aes
import time

MODE_CTR = 6

# Set up the counter with a nonce.
# 64 bit nonce + 64 bit counter = 128 bit output
countf = uos.urandom(8)
#countf = Counter.new(128, nonce)

# 256 bit key
key = uos.urandom(32)

# Instantiate a crypto object first for encryption
cipher = aes(key, MODE_CTR, counter=countf)
encrypted = cipher.encrypt("asdk")
print ('AES-CBC encrypted:', encrypted)

# Reset counter and instantiate a new crypto object for decryption
#countf = Counter.new(64, nonce)
cipher = aes(key, MODE_CTR, counter=countf)
decrypt = cipher.decrypt(encrypted) # prints "asdk"
print ('AES-CBC encrypted:', decrypt)









