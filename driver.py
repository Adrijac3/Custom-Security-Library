from PRF.PRF import *
from CPA.CPA import *
from CCA.CCA import *
from FLHash.FLhash import *
from MerkleDamgard.MerkleDamgard import *
from HMAC.HMAC import * 

g = 47
p = 27527
seed = "10110011011111111111111"

def demoTestPRG():
    g = 47
    p = 27527
    seed = "10110011011111111111111"
    print("seed length: ",len(seed))
    l = lengthExpand(len(seed))
    prn = PRG(seed, l, g, p)
    print("prn length: ",len(prn))
    print("prn: ",prn)

def demoTestPRF():
    g = 47
    p = 27527
    key = "10110011011111111100011111110"
    input = "0000000000000000000000000000000000000000000000000010000101111101"

    prf = PRF(input,key,g,p)
    print("prf input length: ",len(input))
    print("prf input = ", input)
    print("prf output length: ",len(prf))
    print("prf output:" ,prf)

def demoTestCPA():
    BLK_SIZE = 64
    msg = "Hello hi there testing cpa encryption"
    # print("msg in binary : ", msgToBinary(msg))
    # print(binaryToMsg(msgToBinary(msg)))
    key = GEN(p)

    # print("key = ", key)

    r, s = ENC(msg, g, p, key, BLK_SIZE)

    # print("cipher text in binary : ", s)

    m = DEC(r,s, key, g, p, BLK_SIZE)

    print("Decoded msg: ", m)

def demoTestCBCMAC():
    p = 27527
    g = 47
    BLK_SIZE = 64
    msg = "testing out cbc-mac"
    modified_msg = "different msg so tag should not match"
    key = GEN(p)
    tag = CBC_MAC(msg, key, g, p, BLK_SIZE)
    print("tag generated : ",tag)
    print()
    match_res1 = verifyMAC(msg, key, tag, g, p, BLK_SIZE)
    match_res2 = verifyMAC(modified_msg, key, tag, g, p, BLK_SIZE)

    print("original msg :" , msg, "\nmsg sent for verification : ", msg, "\nverification result : ", match_res1)
    print()
    print("original msg :" , msg, "\nmsg sent for verification : ", modified_msg, "\nverification result : ", match_res2)

def demoTestCCA():
    BLK_SIZE = 64

    msg = "Hello hi there testing cca encryption"

    key1 = GEN(p)

    key2 = GEN(p)

    counter , cipher , tag = CCA_ENC(msg, key1, key2, g, p, BLK_SIZE)

    CCAAuthDec(key1, key2, cipher, tag, counter, g, p, BLK_SIZE)

def demoTestFLHash():
    q = 27527
    generator1 = 47
    generator2 = 33
    length = 16

    x1 = GEN(q)
    x2 = GEN(q)

    h = fixedLengthHash(x1, x2, generator1, generator2, q, length)

    print("hash generated with length: ", h)

def demoTestMerkleDamgard():
    q = 27527
    generator1 = 47
    generator2 = 33
    length = 16
    iv= GEN(p)
    iv = iv.zfill(32)
    msg = "0110"
    msg = msgToBinary(msg).zfill(16)
    hash = variableLengthHash(msg, iv, generator1, generator2, q, len(msg) // 2)

    print("Length of input : ", len(msg))
    print(hash)
    print("Length: " + str(len(hash)))

def demoTestHMAC():
    msg = "testing hmac"
    p = 27527
    g = 47
    h = 33
    length = 16
    key = GEN(p)
    iv = GEN(p)
    print("msg : ", msg)
    tag = HMAC(msg, key, iv, g, h, p, length)
    print("tag generated: ", tag)
    print("tag length: ", len(tag))

def displayOptions():
    print()
    print()
    print(" Press 1 for Demo of PRG \n Press 2 for Demo of PRF\n Press 3 for Demo CPA \n Press 4 for CBCMAC demo \n Press 5 for CCA \Press 6 for Fixed Length Hash\n Press 7 for Merkle Damgard\n Press 8 for HMAC: \n Press 0 to exit")
    print()
    print()

def main():
    displayOptions()
    ch = input("select choice")
    while ch != 0:
        if ch == '1':
            demoTestPRG()
            displayOptions()
            ch = input("select choice")
        elif ch == '2':
            demoTestPRF()
            displayOptions()
            ch = input("select choice")
        elif ch == '3':
            demoTestCPA()
            displayOptions()
            ch = input("select choice")
        elif ch == '4':
            demoTestCBCMAC()
            displayOptions()
            ch = input("select choice")
        elif ch == '5':
            demoTestCCA()
            displayOptions()
            ch = input("select choice")
        elif ch == '6':
            demoTestFLHash()
            displayOptions()
            ch = input("select choice")
        elif ch == '7':
            demoTestMerkleDamgard()
            displayOptions()
            ch = input("select choice")
        elif ch == '8':
            demoTestHMAC()
            displayOptions()
            ch = input("select choice")
        elif ch == '0':
            print("EXITING!!!!!")
            exit()
        else:
            print("Invalid input. Try again:")
            displayOptions()
            ch = input("select choice")

main()