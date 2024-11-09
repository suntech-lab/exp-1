import hashlib
import os
import msvcrt
from cryptography.fernet import Fernet

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(64)
    hashbytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 500000) 
    return salt + hashbytes

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

def verify_password(storedpassword, givenpassword):
    salt = storedpassword[:64]
    storedhash = storedpassword[64:]
    providedhash = hashlib.pbkdf2_hmac('sha256', givenpassword.encode('utf-8'), salt, 500000)
    return storedhash == providedhash

def save_password_to_file(password, file_name):
    with open(file_name, 'wb') as file:
        file.write(password)

def read_password_from_file(file_name):
    with open(file_name, 'rb') as file:
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
    key_path = os.path.join(script_directory, 'key.key')
    with open(key_path, 'wb') as key_file:
        key_file.write(key)

def load_key():
    key_path = os.path.join(script_directory, 'key.key')
    return open(key_path, 'rb').read()

def encrypt(file_name, key):
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_name, 'wb') as file:
        file.write(encrypted_data)

def decrypt(file_name, key):
    f = Fernet(key)
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_name, 'wb') as file:
        file.write(decrypted_data)

# Set the path variables relative to this script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))
passwordfile = os.path.join(script_directory, 'password.bin')
file_name = os.path.join(script_directory, 'information.txt')
key_file = os.path.join(script_directory, 'key.key')

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
            if os.path.exists(file_name):
                print('File found.')
                if os.path.exists(key_file):
                    print('Key found.')
                    key = load_key()
                    for i in menu:
                        print(f"enter '{i['input']}' to {i['option']}")
                    user_option_choice = input('\nplease enter here:')
                    for i in menu:
                        if user_option_choice == i['input']:
                            i['func'](file_name, key)
                            break
                    break
                else:
                    get_key()
                    key = load_key()
            else:
                print('File not found. Creating file...')
                open(file_name, 'x').close()
                break
        else:
            print("Password is incorrect.")
    else:
        newpassword = input("Enter a new password: ")
        hashedpassword = hash_password(newpassword)
        save_password_to_file(hashedpassword, passwordfile)
        print("Password saved.")