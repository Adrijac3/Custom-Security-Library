from PRF.PRF import *

'''Function to create Message Authentication code of given msg-
parameters:
  (str) msg : plaintext message
  (str) key: binary key used to create MAC tag
  (int) g : generator for encryption algo
  (int) p : prime for encryption algo
  (int) BLK_SIZE: block size in which message will be divided
return:
  (str) : MAC tag of plaintext
'''
def CBC_MAC(msg, key, g, p, BLK_SIZE):

    msg = str(''.join(format(ord(i), '08b') for i in msg))

    Fk = PRF(decimalToBinary(len(msg)).zfill(64), key, g, p)
    for i in range(0, len(msg), BLK_SIZE):

        m_i = msg[i:i+64].ljust(64,'0')
        m_i = binaryToDecimal(m_i)
        Fk = binaryToDecimal(Fk)

        xor = decimalToBinary(m_i ^ Fk).zfill(64)

        Fk = PRF(xor, key, g, p)
    
    return Fk

'''Function to authenticate MAC
parameters:
  (str) msg: msg whose tag is to be authenticated
  (str) key: binary key used to authenticate MAC tag
  (str) tag: tag against which new tag will be matched
return:
  (bool) True if tag matched, else False
'''
def verifyMAC(msg, key, tag, g, p, BLK_SIZE):
  t = CBC_MAC(msg, key, g, p, BLK_SIZE)
  if t == tag:
    return True
  else:
    return False