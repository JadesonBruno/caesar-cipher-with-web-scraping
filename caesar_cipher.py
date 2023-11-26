# Importing the libraries needed for web scraping
import requests
from lxml import html

# Function to get a random secret word from the web
def load_secret_word():
    url = 'https://www.palavrasaleatorias.com/?fs=1'
    response = requests.get(url)
    page_element = html.fromstring(response.content)
    secret_word = page_element.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')[0].strip()
    return secret_word

# Load the secret word and set the alphabet
key = load_secret_word()
alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ123456789!@#$%^&*(){}[]/? '

# Function that converts the web scraping word into a number, adding the character values and applying modulus 256 (ISO-LATIN-1 Table)
def key_to_number(key):
    return (sum(ord(character) for character in key)) % 256

# Define constants for the application's operating mode (encrypt or decrypt)
ENCRYPT = 1
DECRYPT = 0

# Function that performs the Caesar cipher on a text based on a key
def caesar_cipher(text, key, mode, alphabet):
    processed_text = ""
    alphabet_size = len(alphabet)
    numeric_key = key_to_number(key)

    # Iterate over each character in the input text
    for character in text:
        if character in alphabet:
            character_index = alphabet.index(character)

            # Determines offset based on mode (encrypt or decrypt)
            if mode == ENCRYPT:
                offset = (character_index + numeric_key) % alphabet_size
            elif mode == DECRYPT:
                offset = (character_index - numeric_key) % alphabet_size

            # Get the encrypted or decrypted character through the alphabet
            processed_character = alphabet[offset]
        else:
            # If the character is not in the alphabet, keep it unchanged
            processed_character = character
        # Adds the cryptic character to the encrypted text
        processed_text += processed_character

    return processed_text

# Main function that manages user interaction
def main():

    while True:

        print('''Choose an option:\n1. Encrypt a message\n2. Decrypt a message\n3. Encrypt manually\n4. Decrypt manually\n5. Exit''', end = '\n\n')

        option = input()
        
        if option == '1':
            message = input("Enter the message to be encrypted: ")
            encrypted_message = caesar_cipher(message, key, ENCRYPT, alphabet)
            print("Encrypted message:", encrypted_message)
            print("The key used to encrypt was:", key, end = '\n\n\n')
            
        elif option == '2':
            message = input("Enter the message to be decrypted: ")
            decrypted_message = caesar_cipher(message, key, DECRYPT, alphabet)
            print("Decrypted Message:", decrypted_message)
            print("The key used to decrypt was:", key, end = '\n\n\n')
            
        elif option == '3':
            manual_key = input('Enter the key to encrypt: ')
            message = input("Enter the message to be encrypted: ")
            encrypted_message = caesar_cipher(message, manual_key, ENCRYPT, alphabet)
            print("Encrypted message:", encrypted_message)
            print("The key used to encrypt was:", manual_key, end = '\n\n\n')

        elif option == '4':
            manual_key = input('Enter the key to decrypt: ')
            message = input("Enter the message to be decrypted: ")
            decrypted_message = caesar_cipher(message, manual_key, DECRYPT, alphabet)
            print("Decrypted Message:", decrypted_message)
            print("The key used to decrypt was:", manual_key, end = '\n\n\n')

        elif option == '5':
            print("Program terminated!", end = '\n\n\n')
            break

        else:
            print("Invalid option. Please choose a valid option.", end = '\n\n\n')

# Start executing the program by calling the main function
main()