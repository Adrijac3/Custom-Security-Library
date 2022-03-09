'''Function to convert decimal number to binary-
  parameters:
    (int) n : decimal number
  return:
    (str) : binary representation of n in string datatype
'''
def decimalToBinary(n):
    return bin(n).replace("0b", "")



'''Function to convert binary number to decimal-
parameters:
  (str) b : binary representation of n in string datatype
return:
  (str) : decimal of b
'''
def binaryToDecimal(b):
  return int(b,2)




'''Function to expand length from n bit to poly(n)-
parameters:
  (int) n : bit-size of seed
return:
  (int) : expanded poly(n) length that pseudorandom output will be of
'''
def lengthExpand(n):
    return 2*n




'''function to convert string message to string of binary-
parameters:
  (str) msg: string consisting of plaintext
return:
  (str) : conversion of plaintext to binary representation
'''
def msgToBinary(msg):
    result = ""
    for m in msg:
        result += str(format(ord(m), '08b'))
    global message
    message = result
    return result




'''Function to convert binary string to message string-
parameters:
  (str) binary: binary representation of string
return:
  (str) : string representation of plaintext
'''
def binaryToMsg(binary):
    
    decimal = int(binary, 2)
    decimal_bytes = decimal.to_bytes(decimal.bit_length() + 7 // 8, 'big')
    msg = decimal_bytes.decode('utf-8','surrogatepass')
    return msg or '\0'