# Imports
import sys
import re

# Global variables
inputString = ''
keyString = ''
keyLen = 0
outputString = ''
lenErr = "String length must be at least 1"
alphaErr = "String must be consist only of alphabetic characters and spaces"
alphaSize = 26 # English alphabet
promptText = ''

# Parsing command line arguments
if not hasattr(sys, 'argv'):
    sys.argv  = ['']

cmdUser = ''
sysArgsLen = len(sys.argv)
if sysArgsLen > 1:
	cmdUser = sys.argv[1]
else:
	cmdUser = '-e'


if cmdUser != '-e' and cmdUser != '-d':
	print("Invalid cmd argument:",cmdUser)
	exit(1)

# Prompt to enter plain text
# Check on the validity of input
while len(inputString) == 0:

	if cmdUser != '-e':
		promptText = "Enter a string to decrypt:"
	else:
		promptText = "Enter a string to encrypt:"

	inputString = input(promptText)
	matchPattern = re.fullmatch(r'[a-zA-Z ]+', inputString)
	if matchPattern:
		inputString = inputString.strip(" ")


	if len(inputString) == 0:
		print(lenErr)
	elif not matchPattern:
		print(alphaErr)
		inputString = ''

# Prompt to enter key string
# Check on the validity of input
while len(keyString) == 0:
	keyString = input("Enter a key string: ")
	matchPattern = re.fullmatch(r'[a-zA-Z ]+', keyString)

	if len(keyString) == 0:
		print(lenErr)
	else:
		keyLen = len(keyString)

	if not matchPattern:
		print(alphaErr)
		keyString = ''
	else:
		keyString = keyString.strip(" ")

keyIndex = 0
key = 0

# Encryption/Decryption routine
for i in inputString:
	keyIndex %= keyLen

	if ord(keyString[keyIndex]) >= 97:
		key = ord(keyString[keyIndex]) - 97
	elif ord(keyString[keyIndex]) in range(65,90):
		key = ord(keyString[keyIndex]) - 65
	else:
		keyIndex += 1


	if i == ' ':
		outputString += ' '
		continue

	if ord(i) >= 97:
		if cmdUser == '-e':
			outputString += chr((ord(i) + key - 97) % alphaSize + 97) 
		else:
			outputString += chr((ord(i) - key - 97 + alphaSize) % alphaSize + 97)

	elif ord(i) >= 65:
		if cmdUser == '-e':
			outputString += chr((ord(i) + key - 65) % alphaSize + 65)
		else:
			outputString += chr((ord(i) - key - 65 + alphaSize) % alphaSize + 65)
	
	keyIndex += 1

# Out an encrypted text
print("Encrypted " if cmdUser == '-e'else "Decrypted ", "string:" ,outputString)






