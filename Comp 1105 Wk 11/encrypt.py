from cryptography.fernet import Fernet
# Cryptography module


def read_file():
    with open('test.txt') as content:
        text = content.read()
        print(text)
        key = Fernet.generate_key()
        # Fernet generates a random key
        f = Fernet(key)
        # assign that key to a variable
        encrypt_string = f.encrypt(text.encode())
        # assign the function of encrypting the data you have to a variable
        decrypt_string = f.decrypt(encrypt_string)
        print(encrypt_string)
        # print the encrypted string
        print(decrypt_string)
        # decrypt the string and pring it out


read_file()
