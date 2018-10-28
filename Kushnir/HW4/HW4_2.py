import string

letters_list = list(string.ascii_letters)
print(letters_list)

array2 = []
for i in range(len(letters_list)):
	array2.append(letters_list[i])

def crypto_array():
	for i in range(number):
		array2.append(array2[0])
		array2.remove(array2[0])

print("1) Crypt the text/file")
print("2) Decrypt text from the file")
print("3) Decrypt file from the terminal\n")

try:
	option_input = int(input("[*] Write the number:\n[number] >"))
	if option_input == 1:
		number = int(input("[*] Write the key number [0-%s]: "%(str(len(letters_list)))))

		crypto_array()

		message = input("\n[*] Write the text: \n[text] >> ")
		messagecrd = ""
		for i in message:
			for j in range(len(letters_list)):
				if i == letters_list[j]:
					messagecrd += array2[j]
		crypt = open("text_crypted.txt", "w")
		print("\nCrypt-text: " + messagecrd + "\n")
		crypt.write(messagecrd)
		crypt.close()


	elif option_input == 2:
		number = int(input("[*] Write the key number [0-%s]: "%(str(len(letters_list)))))
		
		crypto_array()
		
		decrypt_r = open("text_crypted.txt", "r")
		read = decrypt_r.read()
		messagedrd = ""
		for i in read:
			for j in range(len(letters_list)):
				if i == array2[j]:
					messagedrd += letters_list[j]
		print("\n Decrypted text: ") 
		print("[text] << " + str(messagedrd))
		answer = input("\n Do you wanna save decrypted text in the file?\n[y/n] > ")
		if answer == "y" or answer == "Y":
			decrypt_w = open("text_decrypt.txt", "w")
			decrypt_w.write(messagedrd)
			decrypt_w.close()
			print("\n[+] File 'text_decrypt.txt' has been successfully created!")
		else:
			pass
		decrypt_r.close()

	elif option_input == 3:
		number = int(input("[*] Write the key number [0-%s]: "%(str(len(letters_list)))))
		
		crypto_array()
	
		message = input("\n [*] Write the crypted text: \n[text] >>")
		messagedrd = ""
		for i in message:
			for j in range(len(letters_list)):
				if i == array2[j]:
					messagedrd += letters_list[j]
		print("\n [*] Decrypted text:")
		print("[text] << " + str(messagedrd))
	else:
		print("The number is not defined!")

except ValueError:
	print("Error! It is acceptable to provide integer numbers ONLY!")

	
		
