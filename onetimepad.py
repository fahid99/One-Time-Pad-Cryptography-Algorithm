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
	for i in range(len(cleartextBin)):
		if len(cleartextBin) == len(keyBin):
			encryptedText = int(cleartextBin[i], 2) ^ int(keyBin[i], 2)
			print(bin(encryptedText), end = " ")

encrypt("Test", "Quiz")

# -------------------------- Decrypt Function --------------------------

def decrypt(ciphertext, key):
	for i in ciphertext:
		decryptedText = ciphertext[i] ^ key[i]
		print(decryptedText)

decrypt(10101000001101001110, 1010001011101010110100101111010)
