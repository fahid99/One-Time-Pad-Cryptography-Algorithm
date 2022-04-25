# Personal Cryptography Projects
These are scripts I've coded to reflect my interest in cryptography and as a way to practice Python coding

# One Time Pad Cipher
My implementation of the one time pad cipher in Python

There are two functions within this code: encrypt() and decrypt()
  - encrypt() has two parameters: cleartext and key (of string type). You use the key to encrypt the cleartext. You return the ciphertext.
  - decrypt() has two parameters: ciphertext and key. You use the same key used to encrypt the cleartext to decrypt the ciphertext. You return the cleartext.
    - When using decrypt(), make sure to prepend '0b' to the ciphertext and key arguments within the decrypt() parameters so Python knows the arguments are binary values.

# RSA Encryption Algorithm
There are two functions within this code: encrypt(), decrypt(), and generateKeys().

These algorithms were created as a way to express my own ideas of how to implement the one time pad cipher and RSA encryption algorithm. Per basic cryptographic safety standards, don't use these files to actually encrypt meaningful data... unless you really want to.

Special shoutout to my pals, Charan R, Varun R, and Micheal B for helping me with my debugging questions.
