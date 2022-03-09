from PRF.PRF import *


'''Function to generate fixed length hash function from to inputs
parameters:
  (str) x1: binary representation of input1 lying between 0 to p-1
  (str) x2: binary representation of input2 lying between 0 to p-1
  (int) g: first primitive root of p
  (int) h: second primitive root of p
  (int) p: prime number p of group Zp*
  (int) length: length of hash to be created
return:
  (str) Binary fixed length hash
'''

def fixedLengthHash(x1, x2, g, h, p, length):
  x1 = binaryToDecimal(x1)
  x2 = binaryToDecimal(x2)
  return decimalToBinary(((owf(g,x1,p) * owf(h,x2,p)) % p)).zfill(length)