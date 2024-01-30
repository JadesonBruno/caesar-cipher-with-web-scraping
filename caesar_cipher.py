# Importing the necessary libraries for web scraping.
import requests
from lxml import html

# Defining constants for the operation mode of the Caesar Cipher.
ENCRYPT = 1
DECRYPT = 0

def load_secret_word():
    """Gets a random secret word from the web."""
    url = 'https://www.palavrasaleatorias.com/?fs=1'
    response = requests.get(url)
    page_element = html.fromstring(response.content)
    secret_word = page_element.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')[0].strip()
    return secret_word

def key_to_number(key):
    """Converts the keyword into a number using the ISO-LATIN-1 table."""
    return sum(ord(character) for character in key) % 256

def caesar_cipher(text, key, mode, alphabet):
    """Performs the Caesar cipher on a text based on a key."""
    processed_text = ""
    alphabet_size = len(alphabet)
    numeric_key = key_to_number(key)

    for character in text:
        if character in alphabet:
            character_index = alphabet.index(character)
            offset = (character_index + numeric_key) % alphabet_size if mode == ENCRYPT else (character_index - numeric_key) % alphabet_size
            processed_character = alphabet[offset]
        else:
            processed_character = character
        processed_text += processed_character

    return processed_text

def get_user_input():
    """Gets user input and validates the option."""
    while True:
        try:
            option = int(input("Choose an option:\n1. Encrypt a message\n2. Decrypt a message\n3. Encrypt manually\n4. Decrypt manually\n5. Exit\n\n"))
            if 1 <= option <= 5:
                return option
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError:
            print("Invalid input. You did not enter a number.")

def main():
    """Loads the secret word from the web and sets the alphabet to be used."""
    key = load_secret_word()
    alphabet = 'abcdefghijklmnopqrstuvwxyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWXYZÀÁÃÂÉÊÓÕÍÚÇ123456789!@#$%^&*(){}[]/? '

    while True:
        option = get_user_input()

        if option == 1 or option == 2:
            message = input(f"Enter the message to be {'encrypted' if option == 1 else 'decrypted'}: ")
            result = caesar_cipher(message, key, option - 1, alphabet)
            print(f"{'Encrypted' if option == 1 else 'Decrypted'} message: {result}")
            print(f"The key used was: {key}\n\n")

        elif option == 3 or option == 4:
            manual_key = input(f"Enter the key to {'encrypt' if option == 3 else 'decrypt'}: ")
            message = input(f"Enter the message to be {'encrypted' if option == 3 else 'decrypted'}: ")
            result = caesar_cipher(message, manual_key, option - 3, alphabet)
            print(f"{'Encrypted' if option == 3 else 'Decrypted'} message: {result}")
            print(f"The key used was: {manual_key}\n\n")

        elif option == 5:
            print("Program terminated!\n\n")
            break

if __name__ == "__main__":
    main()