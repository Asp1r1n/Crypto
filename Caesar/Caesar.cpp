#include <iostream>
#include <cstring>
using namespace std;

int main(){

	const int letters_num = 26; //ASCII TABLE LETTERS
	int key;
	char inputString[100];
	char encryptedString[100];

	cout << "Enter a text to encrypt: ";
	cin >> inputString;
	cout << "Enter a key value(1-26): ";
	cin >> key;

	int length = strlen(inputString);

	for(int i = 0; i < length; i++){
		if(inputString[i] >= 97)
			encryptedString[i] = (inputString[i] + key - 97) % letters_num + 97;
		else if(inputString[i] >= 65)
			encryptedString[i] = (inputString[i] + key - 65) % letters_num + 65;
	}

	encryptedString[length] = '\0';

	cout << "=======================\n";
	cout << "Original  text: " << inputString << endl;
	cout << "Encrypted text: " << encryptedString << endl;

	return 0;
} 
