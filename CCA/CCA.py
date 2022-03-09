from CPA.CPA import *
from CBC_MAC.CBC_MAC import *


'''Function to encrypt msg with key1 and create MAC of cipher text with key2-
parameters:
  (str) msg: plaintext msg to be encrypted
  (str) key1: key to use for encryption
  (str) key2: key to use for creating tag
return:
  (str) r : counter to use for decryption
  (str) cipher: encrypted cipher
  (str) tag: tag of cipher to be verified
'''
def CCA_ENC(msg, key1, key2, g, p, BLK_SIZE):

    r,cipher = ENC(msg, g, p, key1, BLK_SIZE)
    tag = CBC_MAC(cipher, key2, g, p, BLK_SIZE)

    return r, cipher, tag


'''Function to authenticate and decrypt cipher text
parameters:
  (str) key1: key to use for decryption
  (str) key2: key to use for matching tag
  (str) cipher: encrypted cipher
  (str) tag: tag of cipher against which new tag will be matched
  (str) counter: counter to use for decryption
return:
  (void)
'''
def CCAAuthDec(key1, key2, cipher, tag, counter, g, p, BLK_SIZE):
    
    counter = counter.zfill(64)

    #authenticate, if passed, then decrypt
    match_res = verifyMAC(cipher, key2, tag, g, p, BLK_SIZE)
    
    if match_res == 1:

      print("MAC VERIFIED. NOW PROCESSING FOR DECRYPTION")
      m = DEC(counter, cipher, key1, g, p, BLK_SIZE)
      print("Decoded msg: ", m)
      return

    else:
      print("MAC VERIFICATION FAILED. EXITING WITHOUT DECRYPTION!!!!!")
      return