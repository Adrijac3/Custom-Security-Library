from FLHash.FLhash import *


### Defining ipad and opad and expanding as many times needed
ipad = (decimalToBinary(0x5c)).zfill(8)
opad = (decimalToBinary(0x36)).zfill(8)

for i in range(0,2):
    ipad += ipad
    opad += opad

'''Function to create MAC from fixed length hash
parameters:
  (str) msg: plaintext to authenticate
  (str) key: common secret key to authenticate
  (str) iv: random initial vector
  (int) g: 1st primitive root of prime p
  (int) h: 2nd primitive root of prime p
  (int) p: prime p of group Zp*
  (int) length: length of fixed hashing

return:
  (str): h-mac code of given msg
'''   

def HMAC(msg, key, iv, g, h, p, length):

  msg = msgToBinary(msg)

  ipad_xor = decimalToBinary(binaryToDecimal(key) ^ binaryToDecimal(ipad))
  opad_xor = decimalToBinary(binaryToDecimal(key) ^ binaryToDecimal(opad))


  L = len(msg)
  L = decimalToBinary(L)

  ipad_xor = ipad_xor.zfill(length)
  opad_xor = opad_xor.zfill(length)
  iv = iv.zfill(length)
  L = L.zfill(length)

  x2 = fixedLengthHash(ipad_xor, iv, g, h, p, length)

  for i in range(0, len(msg), length):

    x1 = msg[i : i + length].ljust(length, '0')
    x2 = fixedLengthHash(x1, x2, g, h, p, length)

  x1 = fixedLengthHash(L, x2, g, h, p, length)
  x2 = fixedLengthHash(opad_xor, iv, g, h, p, length)

  result = fixedLengthHash(x1, x2, g, h, p, length)

  return result