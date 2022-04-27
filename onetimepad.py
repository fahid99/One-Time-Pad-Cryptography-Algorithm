import random

def encrypt(cleartext, key):

	# ------------------------- Changing cleartext into binary values -------------------------

	cleartextList = list(cleartext)
	cleartextASCII = []
	cleartextBin = []

	for i in cleartextList:
		cleartextASCII.append(ord(i))

	for i in cleartextASCII:
		cleartextBin.append(bin(i))

	# ------------------------- Changing key into binary values -------------------------

	keyList = list(key)
	keyASCII = []
	keyBin = []

	for i in keyList:
		keyASCII.append(ord(i))
	
	for i in keyASCII:
		keyBin.append(bin(i))

	print("\n---------- This is the binary representation of the key. Keep it a secret! ----------")
	print(keyBin)

	# -------------------------- XOR'ing the cleartext and private key to generate the ciphertext --------------------------
	ciphertextASCII = []

	if len(cleartext) == len(key):
		print("\n---------- This is the binary representation of the encrypted text ----------")
		for i in range(len(cleartextBin)):
			ciphertext = int(cleartextBin[i], 2) ^ int(keyBin[i], 2)
			print(bin(ciphertext), end = " ")
			ciphertextASCII.append(ciphertext)
		print("")
	else:
		print("The text cannot be encrypted securely since the text and key are not of equal bit size")

	return ciphertextASCII
	
encrypt("Tests", "Fahid")

# -------------------------- XOR'ing the ciphertext and private key to decrypt the ciphertext --------------------------

def decrypt(ciphertext, key):
	cleartextBin = []

	for i in range(len(ciphertext)):
		cleartextBin.append(ciphertext[i] ^ key[i])

	res = ""
	for i in cleartextBin:
		res += chr(i)
	print(res)

print("---------- This is the decrypted message ----------")
decrypt([0b10010, 0b100, 0b11011, 0b11101, 0b10111],[0b1000110, 0b1100001, 0b1101000, 0b1101001, 0b1100100])

def hashPassword(password):
	p = random.randint(10000,99999999)
	q = random.randint(10000,99999999)
	n = random.randint(1,5)

	for i in range(p):
		if (i % 2 != 0):
			p = (i % 2 != 0)
			return p
			
	for i in range(q):
		if (i % 2 != 0):
			q = (i % 2 != 0)
			return p

	res = p * q

	encryptedPassword = encrypt(password, input())
	hashedPassword = ord(bin(res % len(encryptedPassword)) ^ bin(encryptedPassword) - n)
	return hashedPassword

hashPassword("hello")
