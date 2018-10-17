import sys
import re

# RSA ----------------------------------------------

#Exponentiation by squaring O(log n)
def power(x,n):
	if n == 1:
		return x
	elif n % 2 == 0:
		return power(x * x, n/2)
	elif n > 2 and n % 2 != 0:
		return x * power(x * x, (n-1)/2)

def encrypt(m,e,n):
	return power(m,e) % n

def decrypt(c,d,n):
	return power(c,d) % n

p = 769 #prime
q = 971 #prime
n = p * q # 769 * 971 = 746 699
totient = (p - 1) * (q - 1) # 768 * 970 = 744 960
e = 19 # coprime for totient
#k = 7 
#c = 1 + k * totient
# d * e = c
d = 274459
# public key (n,e) {746 699, 19}
# ptivate key (n,d) {746 699, 274 459}
#----------------------------------------------------

# Global variables
inputString = ""
resultString = ''
inputStringChars = []
inputStringInitChars = []
inputStringResultChars = []
lenErr = "String length must be at least 1"
alphaErr = "String must be consist only of alphabetic characters and spaces"

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

	matchPattern = ''
	if cmdUser != '-e':
		promptText = "Enter a string to decrypt:"
	else:
		promptText = "Enter a string to encrypt:"

	inputString = input(promptText)
	if cmdUser != '-e':
		matchPattern = re.fullmatch(r'[0-9@]+', inputString)
	else:
		matchPattern = re.fullmatch(r'[a-zA-Z ]+', inputString)
	if matchPattern:
		inputString = inputString.strip(" ")


	if len(inputString) == 0:
		print(lenErr)
	elif not matchPattern:
		print(alphaErr)
		inputString = ''



# Encryption/Decryption routine
if cmdUser == '-e':
	inputStringChars = list(inputString)
	for i in range(len(inputStringChars)):
		inputStringInitChars.append(ord(inputStringChars[i]))

	for i in range(len(inputStringInitChars)):
		inputStringResultChars.append(encrypt(inputStringInitChars[i],e,n))
		resultString += str(inputStringResultChars[i]) + "@"
	resultString = resultString[0:len(resultString) - 1]
	print("Encrypted string: ",resultString, sep='')
else:
	inputStringInitChars = inputString.split("@",inputString.count("@"))
	for i in range(len(inputStringInitChars)):
		inputStringResultChars.append(decrypt(int(inputStringInitChars[i]),d,n))
		resultString += chr(inputStringResultChars[i])
	print("Decrypted string: ",resultString, sep='')









