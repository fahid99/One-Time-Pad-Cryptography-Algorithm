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

	print(cleartextBin, keyBin)
	# -------------------------- XOR --------------------------
	for i in range(len(cleartextBin)):
		if len(cleartextBin) == len(keyBin):
			encryptedText = int(cleartextBin[i], 2) ^ int(keyBin[i], 2)
			print(bin(encryptedText))

	encrypt("Test", "1n3f")


# -------------------------- Decrypt Function --------------------------
def decrypt(ciphertext, key):

	keyList = list(key)
	keyASCII = []
	keyBin = []

	for i in keyList:
		keyASCII.append(ord(i))
	
	for i in keyASCII:
		keyBin.append(bin(i))

	for i in range(len(ciphertext)):
		encryptedText = int(ciphertext[i], 2) ^ int(keyBin[i], 2)
		print(bin(encryptedText))
