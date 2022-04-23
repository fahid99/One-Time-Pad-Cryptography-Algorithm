def encrypt(cleartext, key):

	# ------------------------- cleartext -------------------------

	cleartextList = list(cleartext)
	cleartextASCII = []
	cleartextBin = []

	for i in cleartextList:
		cleartextASCII.append(ord(i))

	for i in cleartextASCII:
		cleartextBin.append(bin(i))

	# ------------------------- key -------------------------

	keyList = list(key)
	keyASCII = []
	keyBin = []

	for i in keyList:
		keyASCII.append(ord(i))
	
	for i in keyASCII:
		keyBin.append(bin(i))

	print("----------This is the binary representation of the cleartext and private key, respectively----------")
	print(cleartextBin, keyBin)

	# -------------------------- XOR --------------------------

	print("----------This is the encrypted text in binary----------")
	if len(cleartextBin) == len(keyBin):
		for i in range(len(cleartextBin)):
			ciphertext = int(cleartextBin[i], 2) ^ int(keyBin[i], 2)
			if len(keyBin) == len(ciphertext):
				print(bin(ciphertext), end = " ")
			else:
				print("Cannot be encrypted")
	else:
		print("The text cannot be encrypted securely since the text and key are not of equal bit length")

encrypt("Test", "Quiz")

# -------------------------- Decrypt Function --------------------------

def decrypt(ciphertext, key):
	for i in ciphertext:
		decryptedText = ciphertext[i] ^ key[i]
		print(decryptedText)

decrypt(10101000001101001110, 1010001011101010110100101111010)
