from PRG.PRG import *


'''Function to create PRF from PRG-
parameters:
  (str) input: n- bit binary input to the PRF function
  (str) key: randomly chosen key in binary representation (used as initial seed for PRG)
  (int) l: expanded length of input
  (int) g: generator
  (int) p: prime
return:
  (str) : output of prf in binary with n-bit (same as no. of bits in input)
'''

def PRF(input,key,g,p):
    n = len(input)
    i_ = 0
    for i in input:
        b = PRG(key,2*n,g,p)
        if i == '0':
            key = b[0:n]
        else:
            key = b[n:]
    return key