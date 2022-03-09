from PRF.PRF import *

'''Function to generate key-
parameters:
  (int) p: prime of group Zp. Our valid set of keys will lie between (0, p-2) as the generator can have powers between this range.
return:
  (str) : binary format of chosen key
'''
def GEN(p):
    
    seed = randint(0, p-2)
    seed = decimalToBinary(seed)
    return seed
    

def msgToBinary(msg):
    result = ""
    for m in msg:
        result += str(format(ord(m), '08b'))
    global message
    message = result
    return result
  

'''Function to encrypt plaintext-
parameters:
  (str) msg: plaintext
  (int) g: generator
  (int) p: prime of group Zp
  (str) key: binary representation of randomly chosen key
  (int) BLK_SIZE: blocksize to divide message into
return:
  (str) orig_counter: random noise used
  (str) cipher: cipher text
'''
def ENC(msg, g, p, key, BLK_SIZE):
    print(msg)
    msg = msgToBinary(msg)
    l = 2*len(key)
    cipher = ""
    orig_counter = GEN(p).zfill(BLK_SIZE)
    counter = orig_counter

    for i in range(0, len(msg), BLK_SIZE):
        counter = decimalToBinary(binaryToDecimal(counter) + 1).zfill(BLK_SIZE)
        Fk = PRF(counter, key, g, p)
        m_i = msg[i: i + BLK_SIZE]
        Fk = Fk[0:len(m_i)]
        m_i = binaryToDecimal(m_i)
        Fk = binaryToDecimal(Fk)

        cipher += decimalToBinary(m_i ^ Fk)
    return orig_counter, cipher


'''Function to decrypt ciphertext-
parameters:
  (str) counter: random noise
  (str) cipher: ciphertext
  (str) key: binary representation of randomly chosen key
  (int) BLK_SIZE: blocksize to divide message into
return:
  (str) decoded plaintext
'''
def DEC(counter, cipher, key, g, p,BLK_SIZE):
    result = ""
    for i in range(0, len(cipher), BLK_SIZE):
        counter = decimalToBinary(binaryToDecimal(counter) + 1).zfill(BLK_SIZE)
        Fk = PRF(counter, key, g, p)
        c_i = cipher[i:i + BLK_SIZE]
        Fk = Fk[0:len(c_i)]
        c_i = binaryToDecimal(c_i)
        Fk = binaryToDecimal(Fk)

        result += decimalToBinary(c_i ^ Fk)


    # print("decoded msg to binary: ",message)
    return binaryToMsg(message)