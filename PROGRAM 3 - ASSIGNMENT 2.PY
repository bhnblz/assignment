# Import pyfiglet module to change the font
import pyfiglet

# Import colorama module to change the color of the font
import colorama 
from colorama import Fore

title = "The Vigenere Cipher"
print(pyfiglet.figlet_format(title, font = "digital") + Fore.LIGHTCYAN_EX)

# Ask for the input
message = input("What is the message? " + Fore.LIGHTCYAN_EX)
keyword = input("What is the keyword? " + Fore.LIGHTCYAN_EX)

# Encrypt the plaintext using Vigenere Cipher
def encrypt_plaintext(message, key):
    ciphertext = ""
    key_length = len(key)
    for j in range(len(message)):
        val = message[j]
        key_val = key[j % key_length]
    # Add a value to the ciphertext variable
        ciphertext += chr((ord(val) + ord(key_val)) % 26 + 65)
    return ciphertext

ciphertext = encrypt_plaintext(message, keyword)

# Print the output
print("=" * 44)
print(Fore.LIGHTMAGENTA_EX + ("\033[7mThe ciphertext is: " + ciphertext))