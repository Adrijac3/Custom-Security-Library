
from utilities.utilities import *
from random import randint


'''function to get hardcore predicate bit using Goldreich-Levin Theorem-
parameters:
  (str) x : input of one-way function 
return:
  (str) : 1 bit hardcore predicate of x
'''
def hc(x):
    n = len(x)//2 
    b = 0
    for i in range(0,n):
        b = b ^ ( int(x[i]) & int(x[i+n]) )
    return str(b)

'''ONE-WAY function (candidate = DLP)-
   parameters: 
    (int) x: input
    (int) g: generator of group
    (int) p: prime of  Zp
  return:
    (int) b : dlp of input
'''
def owf(x,g,p):
    return pow(g,x,p)


'''Function to generate PRN of length_expand(n) bits from a seed-
parameters:
  (str) seed: binary representation of seed
  (int) l : length to which output of PRG is to be extended
  (int) g: generator of group
  (int) p : prime o f Zp
return:
  (str) : pseudorandomly generated number of l(n) length
'''
def PRG(seed, l, g, p):
    x = seed
    hcp = hc(x)
    prn = str(hcp)
    while l > 1 :
        l -= 1
        x =  decimalToBinary(owf(binaryToDecimal(x),g,p))
        hcp = hc(x)
        prn += str(hcp)
    return prn