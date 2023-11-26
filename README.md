# Caesar Cipher with Web Scraping

[![License](https://img.shields.io/npm/l/react)](https://github.com/JadesonBruno/caesar_cipher_with_web_scraping/blob/main/LICENSE)

## About the Project

In this project we will explore a data encryption and decryption technique that will be implemented in Python. The project in focus is an implementation of the Caesar Cipher, a classic encryption technique that allows the encryption and decryption of messages using a "shift key". Additionally, we will highlight the incorporation of Web Scraping techniques to obtain a random secret key, a crucial component of encryption.

It is a type of substitution cipher, in which one letter in the original text is replaced by another, using a shift key.

![Caesar Cipher Example](https://github.com/JadesonBruno/caesar_cipher_with_web_scraping/blob/main/assets/caesar_cipher.png)

In the example in the image, considering that we had a collection of characters represented only by uppercase letters, we would have a shift key numbered 3:

- Alphabet without encryption: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
- Alphabet with cipher: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

The Caesar Cipher is a historical example of cryptography that still has relevance today. However, it is important to emphasize that its use, in isolation, would not be effective, given the current information security scenario.

This project was a prerequisite for approval in the “Programming Logic I” module of the “Vem Ser Tech Course - Data powered [Ifood](https://www.ifood.com.br/) | Data Analystic” from the educational institution [Ada Tech](https://ada.tech/).

## Objectives

The objective of this project is to encrypt and decrypt messages using a common key.

1. In this project, users must enter a message that will be encoded or decoded.
2. Users must choose between encryption with Web scraping (1), decryption with Web Scraping (2), manual encryption (3) or manual decryption (4) options.
3. Every time the code is executed, the key coming from Web Scraping changes. To overcome this limitation, options (3) and (4) were created, since, once you have the key, it will be possible to perform encryption or decryption manually.
4. Using the same key, the application must process the encryption or decryption of the same message.
5. Two different keys must generate different encryptions and/or decryptions.

## Code Overview

Here are the main components of the code:

1. Importing Libraries:
- The code starts by importing the necessary libraries, in this case, `requests` to make HTTP requests and `lxml` to do Web Scrapping. These libraries are essential to obtain a random secret key from the web.

2. `load_secret_word` function:
- This function uses Web Scraping to obtain a random secret word from a website. The secret word is essential for generating the "shift key".

3. Key and Alphabet:
- The secret word is loaded and stored in the `key` variable. The alphabet used in the encryption process is defined in the `alphabet` variable.

4. `key_to_number` function:
- This function converts a key into a number by adding the values corresponding to the Unicode of the characters, through the `ord` function, and applies modulo 256. This is crucial to determine the "shift key" used in the Caesar Cipher.

5. Definition of Constants:
- Two constants were defined, `ENCRYPT` and `DECRYPT`, which represent the encryption and decryption modes, respectively.

6. `caesar_cipher` function:
- This is the main function of the code, it performs the Caesar Cipher on a text based on a specified key and mode. It will iterate over each character in the input text, calculate the offset based on the key and mode, and return the ciphered or deciphered text.

7. `main` function:
- Program execution is started by calling the `main()` function. It manages user interaction by allowing the user to choose between encrypting, decrypting, encrypting using a manual key, decrypting using a manual key, or exiting the program. Depending on the user's choice, the program performs the corresponding operations.

This code overview provides an initial understanding of the essential parts of the project, from the encryption functions to the use of web scraping to obtain the secret key.

### Web Scraping

The scraping part of this code is responsible for making a request to a web page, extracting specific information from the content of that page and then returning the secret word that will be used as a key to encrypt and decrypt messages.

Here is the detailed explanation of the scraping part:

1- Importing libraries:
- The code starts by importing the necessary libraries, including requests and lxml.html. requests is used to make HTTP requests to the web server, and lxml.html is used to parse and extract information from the HTML content of the web page.

2- Definition of the secret_word_load function:

- The secret_word_load function is created to perform the scraping task.
- Sets the url variable to the URL of the web page that contains the secret word. In this case, the URL is 'https://www.palavrasaleatorias.com/?fs=1'.
- Uses requests.get(url) to make an HTTP request to the page and store the response in the response variable.
- The response contains the HTML content of the page.
- It then uses the lxml.html library to create an object called page_element from the HTML content of the response.
- Uses the .xpath() function to extract text from the page that is inside an HTML element that corresponds to //div[@style="font-size:3em; color:#6200C5;"]/text(). This XPath expression identifies the DIV element with the specified "style" attribute and extracts the text contained within it.
- The secret word is obtained from the first item in the list resulting from the .xpath() function, removing white spaces with .strip().
- The function returns the secret word.

3- Secret key:

- The Load_Secret_Word() function is called to obtain the secret word. It is assigned to the key variable. The secret word is used as a key to encrypt and decrypt messages.

![Scrapping Website](https://github.com/JadesonBruno/caesar_cipher_with_web_scraping/blob/main/assets/site_web_scraping.png)

![Web Scrapping Element](https://github.com/JadesonBruno/caesar_cipher_with_web_scraping/blob/main/assets/html_element_web_scraping.png)

```python
    def load_secret_word():
      url = 'https://www.palavrasaleatorias.com/?fs=1'
      response = requests.get(url)
      page_element = html.fromstring(response.content)
      secret_word = page_element.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')[0].strip()
      return secret_word
```

## Project Flowchart

![Project Flowchart](https://github.com/JadesonBruno/caesar_cipher_with_web_scraping/blob/main/assets/project_flowchart.png)

## Technologies Used

- Python 3.10.9
- Lucidchart

## How to execute the project

To run this code, you will need a Python environment installed on your machine. Here are the steps you can follow:

1- Install the required libraries:
Open a terminal or command prompt and run the following commands to install the required libraries.


```bash
pip install requests
pip install lxml
```

In version 3.10.9 these libraries are already installed with the Python environment.

2- Copy the code:
Copy the provided Python code.

3- Paste the code into a Python file:
Open your favorite text editor or Python development environment and paste the code into a new file with the .py extension. For example, you can save the file as caesar_cipher.py.

4- Run the script:
In the terminal or command prompt, navigate to the directory where you saved the Python file and run it using the command:

```bash
python caesar_cipher.py
```
This will launch the program and you will be asked to choose an option. Follow the instructions in the console to encrypt, decrypt, or exit the program.

Make sure you have an active internet connection, as the program does web scraping to obtain a random secret word.

## Contributions

Contributions are welcome! Feel free to suggest improvements or corrections to the project.

## Author

Jadeson Bruno Albuquerque da Silva

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jadeson-bruno-228450101/)
