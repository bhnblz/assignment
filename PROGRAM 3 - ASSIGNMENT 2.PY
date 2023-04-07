# Import pyfiglet module to change the font style
import pyfiglet

# Import colorama module to change the color of the font
import colorama
from colorama import Fore

title = "The Vigenere Cipher"
print(pyfiglet.figlet_format(title, font = "digital") + Fore.LIGHTCYAN_EX)

# Use Vigenere Cipher to encrypt the plaintext
def encrypt_plaintext(message, keyword):
    ciphertext = ""
    index = 0
    for i in message:
        if i.isalpha():
        # Convert to numerical value
            message_val = ord(i) - 65
            key_val = ord(keyword[index]) - 65
            index = (index + 1) % len(keyword)
        # Encrypt the plaintext using the keyword
            ciphertext_val = (message_val + key_val) % 26
        # Convert to letter
            ciphertext_char = chr(ciphertext_val + 65)
        # Add ciphertext_char variable to ciphertext variable
            ciphertext += ciphertext_char
        else:
            ciphertext += i
    return ciphertext

# Ask for the input
message = input("What is the message? " + Fore.LIGHTCYAN_EX)
keyword = input("What is the keyword? " + Fore.LIGHTCYAN_EX)

ciphertext = encrypt_plaintext(message, keyword)

# Print the output
print("=" * 45)
print("*" * 45)
print(Fore.LIGHTMAGENTA_EX + ("\033[7mThe ciphertext is: " + ciphertext))