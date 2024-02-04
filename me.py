import hashlib
import os
import msvcrt
from cryptography.fernet import Fernet
import random
import string

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(64)
        #salt = ''.join(random.choice(string.ascii_letters) for i in range(64))
    hashbytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 500000) 
    #print(str(salt + hashbytes))
    return salt + hashbytes

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def verify_password(storedpassword, givenpassword):
    salt = storedpassword[:64]
    storedhash = storedpassword[64:]
    providedhash = hashlib.pbkdf2_hmac('sha256', givenpassword.encode('utf-8'), salt, 500000)
    return storedhash == providedhash

def save_password_to_file(password, filename):
    with open(filename, 'wb') as file:
        file.write(password)

def read_password_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def mask_input(prompt):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n':
            print()
            break
        elif char == '\b':
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    return password

def get_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    return open('key.key', 'rb').read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)

def decrypt(filename, key): #KEY CHANGES, UNABLE TO DECRYPT
    f = Fernet(key) #KEY CHANGES, UNABLE TO DECRYPT
    with open(filename, 'rb') as file: #KEY CHANGES, UNABLE TO DECRYPT
        encrypted_data = file.read() #KEY CHANGES, UNABLE TO DECRYPT
        decrypted_data = f.decrypt(encrypted_data) #KEY CHANGES, UNABLE TO DECRYPT
        with open(filename, 'wb') as file: #KEY CHANGES, UNABLE TO DECRYPT
            file.write(decrypted_data) #KEY CHANGES, UNABLE TO DECRYPT



passwordfile = '#######.bin'

laptop_location = 'C:/Users/ericl/Documents/lab'

desktop_location = 'C:/Users/Eric/Desktop/FunnyPrograms'

file_name = 'information.txt'

menu = [
        {'input': 'decrypt', 'option': 'decrypt', 'func': decrypt},
        {'input': 'encrypt', 'option': 'encrypt', 'func': encrypt}
]

while True:

    if os.path.exists(passwordfile):

        storedpassword = read_password_from_file(passwordfile)
        passwordtoverify = mask_input("Enter the password to verify: ")

        if verify_password(storedpassword, passwordtoverify):
            print("Password is correct.")
            get_key()
            key = load_key()

            if find(file_name, laptop_location) or find(file_name, desktop_location):
                print('File found.')

                for i in menu:
                    print(f"enter '{i['input']}' to {i['option']}")

                user_option_choice = input('\nplease enter here:')

                for i in menu:
                    if user_option_choice == str(i['option']):

                        i['func'](file_name, key)
                        break

                with open(file_name, 'a') as f:
                    info = input('What would you like to add to information.txt?\n:')
                    f.write(info)

                break

            elif not find(file_name, laptop_location) or not find(file_name, desktop_location):
                print('File not found. Creating file...')

                open(file_name, 'x')
                
                break
            
        else:
            print("Password is incorrect.")
    else:
        newpassword = input("Enter a new password: ")
        hashedpassword = hash_password(newpassword)

        save_password_to_file(hashedpassword, passwordfile)
        print("Password saved.")
