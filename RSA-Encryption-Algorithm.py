import random

def generateKeys():
    # -------------------- Generate encryption key pair --------------------
    p = random.randint(2,100)
    q = random.randint(2,100)

    # finds the prime numbers that'll later be p and q
    # we want to find encrypt(val1, val2) such that val1 and val 2 is the encryption key pair
    for i in range(p):
        if (i % 2 != 0):
            p = (i % 2 != 0)

    for i in range(q):
        if (i % 2 != 0):
            q = (i % 2 != 0)

    #res is actually val2
    res = p * q
    print(res)

    # finds the factors of res
    phi = []
    for i in range(1, res+1):
        if res % i != 0:
            phi = i.append

    # computing encryption keys. e is actually val1. We now have encrypt(val1, val2)
    for e in range(1,phi[-1]):
        if (e > 1) & (e < phi[i]):
            print(e)

    def encrypt(cleartext):
        cleartextList = list(cleartext)
        cleartextASCII = []
        ciphertext = []

        # converts cleartext to corresponding ASCII values
        for i in cleartextList:
            cleartextASCII.append(ord(i))

        # creates the ciphertext
        for i in range(len(cleartextASCII)):
            ciphertext.append((cleartextASCII[i] ** e) % res)
        print("The cleartext -- " + cleartext + " -- is now encrypted as ciphertext: ")
        print(ciphertext)
