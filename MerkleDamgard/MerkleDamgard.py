from FLHash.FLhash import *


'''Function to generate variable length hash from fixed length hash using Merkle-Damgard Transform
parameters:
  (str) msg : input whose hash is to be generated
  (str) initial_vector: random chosen noise
  (int) g: first primitive root of p to pass to inner hash function
  (int) h: second primitive root of p to pass to inner hash function
  (int) p: prime number p of group Zp*
  (int) fixed_length: length of fixed hash to be created inside
return:
  (str) : Binary hash of length n/2
'''
def variableLengthHash(msg, initial_vector, g, h, p, fixed_length):
  
  L = len(msg)
  L = decimalToBinary(L).zfill(fixed_length)
  x2 = initial_vector

  for i in range(0, len(msg), fixed_length):

    x1 = msg[i : i + fixed_length].ljust(fixed_length,'0')
    x2 = fixedLengthHash(x1, x2, g, h, p, fixed_length)

  result = fixedLengthHash(L, x2, g, h, p, fixed_length)

  return result