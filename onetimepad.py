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

	print("---------- This is the binary representation of the cleartext and private key, respectively ----------")
	print(cleartextBin, keyBin)

	# -------------------------- XOR'ing the cleartext and private key to generate the ciphertext --------------------------

	if len(cleartext) == len(key):
		print("---------- This is binary representation of the encrypted text ----------")
		for i in range(len(cleartextBin)):
			ciphertext = int(cleartextBin[i], 2) ^ int(keyBin[i], 2)
			print(bin(ciphertext), end = " ")
	else:
		print("The text cannot be encrypted securely since the text and key are not of equal bit length")

# EXAMPLE: encrypt("cat", "hat")

# -------------------------- XOR'ing the ciphertext and private key to decrypt the ciphertext --------------------------

def decrypt(ciphertext, key):

	ciphertext = []
	key = []
	
	cleartext = []
	for i in range(len(ciphertext)):
		cleartext = ciphertext ^ key
		cleartext.append(ord(i))
	print("\n---------- This is the decrypted text ----------")
	print(cleartext)

# EXAMPLE: decrypt([0b1011000, 0b0000000, 0b0000000],[0b1101000, 0b1100001, 0b1110100])
