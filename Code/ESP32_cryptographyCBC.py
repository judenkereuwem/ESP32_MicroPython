###################################################
#             AES CBC Cryptography              #
###################################################

import uos
from ucryptolib import aes
import time

#start time
st = time.ticks_cpu()

# CBC MODE
MODE_CBC = 2

#Define blocksize
BLOCK_SIZE = 16
 
# key size must be 16 or 32
# key = uos.urandom(32)
key = b'I_am_32bytes=256bits_key_padding'
 
data = 'This is AES cryptographic'
print('Raw Data:', data)

# Padding plain text with space 
pad = BLOCK_SIZE - len(data) % BLOCK_SIZE
data = data + " "*pad
 
# Generate iv with HW random generator 
iv = uos.urandom(BLOCK_SIZE)
cipher = aes(key,MODE_CBC,iv)
 
encrypted = iv + cipher.encrypt(data)
print ('\nEncrypted Data:', encrypted)
 
iv = encrypted[:BLOCK_SIZE]
cipher = aes(key,MODE_CBC,iv)
decrypted = cipher.decrypt(encrypted)[BLOCK_SIZE:]
print('\nDecrypted Data:', decrypted)

# get the end time
et = time.ticks_cpu()

# get execution time
res = et - st
print('\nExecution time:', res, 'seconds')
