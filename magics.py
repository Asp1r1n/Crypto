import sys
import re
import math
inputString = ''
outputString = ''
lenErr = "String length must be at least 1"
alphaErr = "String must be consist only of alphabetic characters and spaces"
promptText = ''
magicSquares = ["Pandiagonal"]
magicSquaresMode = [["Block","Symbol"]]
userMS = 0
userMSM = 0
square = []
squareCode = ["","","","",
			  "","","","",
			  "","","","",
			  "","","",""]

def buildSquare():

	if userMS == '1': #Pandiagonal
		a = 1
		b = 2
		c = 1
		d = 4
		e = 8
		square = [a, a+b+c+e, a+c+d, a+b+d+e,
				 a+b+c+d, a+d+e, a+b, a+c+e,
				 a+b+e, a+c, a+b+c+d+e, a+d,
				 a+c+d+e, a+b+d, a+e, a+b+c]

	return square

def printSquare(square):
	for i in range((len(square) // 4)):
		for j in range(4):
			index = j + i * 4
			print(" " + str(square[index]) if square[index] < 10 else square[index] ,sep=' |',end=' ')
		print()

def printSquareCode(square,code):
	for i in range((len(square) // 4)):
		for j in range(4):
			index = j + i * 4
			print(" " + str(square[index]) if square[index] < 10 else square[index] , \
			 " - ", squareCode[index] ,sep='',end=' ')
		print()



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



promptText = "Choose the method of magic square: "
print(promptText)
for i in range(len(magicSquares)):
	print("\t",i + 1, " - ", magicSquares[i],sep='')
while userMS != '1':
	userMS = input("Input >>> ")

if cmdUser == '-e':
	promptText = "Choose the encryption mode: "
else:
	promptText = "Choose the decryption mode: "

print(promptText)
index = int(userMS) - 1
for i in range(len(magicSquaresMode[index])):
	print("\t",i + 1, " - ", magicSquaresMode[index][i],sep='')
while int(userMSM) < 1 or int(userMSM) > 2:
	userMSM = input("Input >>> ")

	if not userMSM.isdecimal():
		userMSM = 0
	


print("Generated square: ")

square = buildSquare()
print(square)
printSquare(square)


# Prompt to enter plain text
# Check on the validity of input
while len(inputString) == 0:

	if cmdUser != '-e':
		promptText = "Enter a string to decrypt:"
	else:
		promptText = "Enter a string to encrypt:"

	inputString = input(promptText)
	matchPattern = re.fullmatch(r'[a-zA-Z ]+', inputString)


	if len(inputString) == 0:
		print(lenErr)
	elif not matchPattern:
		print(alphaErr)
		inputString = ''

if userMSM == '1':
	if cmdUser == '-e':
		chunksSize = math.ceil(len(inputString) / 16)
		chunks=[inputString[i:i+chunksSize] for i in range(0, len(inputString), chunksSize)]
		for chunk in range(len(chunks)):
			for val in range(len(square)):
				if (chunk + 1) == square[val]:
					squareCode[val] = chunks[chunk]
					break;

		printSquareCode(square,squareCode)
		for i in squareCode:
			if i != '':
				outputString += i
				if len(i) != chunksSize:
					for j in range(len(i),chunksSize):
						outputString += " "
			else:
				for j in range(chunksSize):
					outputString += " "
	else:
		chunksSize = math.ceil(len(inputString) / 16)
		chunks = [inputString[i:i+chunksSize] for i in range(0, len(inputString), chunksSize)]
		for chunk in range(len(chunks)):
			squareCode[chunk] = chunks[chunk]
		printSquareCode(square,squareCode)
		


		for i in range(len(squareCode)):
			for chunk in range(len(square)):
				if i+1 == square[chunk]:
					outputString += squareCode[chunk]
					break
else:
	print("Symbol")


print("Encrypted " if cmdUser == '-e'else "Decrypted ", "string:" , outputString if cmdUser == '-e' else outputString.strip(" "), end=".\n")
