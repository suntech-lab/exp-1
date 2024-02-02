import hashlib
import os
import msvcrt
from cryptography.fernet import Fernet

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(64) # generate a 64 byte salt
    hashbytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 500000) 
    return salt + hashbytes

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def verify_password(storedpassword, givenpassword):
    salt = storedpassword[:64] # remove the salt
    storedhash = storedpassword[64:] # remove the hash
    providedhash = hashlib.pbkdf2_hmac('sha256', givenpassword.encode('utf-8'), salt, 500000)
    return storedhash == providedhash

def save_password_to_file(password, filename):
    with open(filename, 'wb') as file:
        file.write(password) # write the hashed and salted password into the password file

def read_password_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read() # read the hashed and salted password

def masked_input(prompt):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r' or char == '\n': # if enter is pressed it prints and breaks out of the loop
            print()
            break
        elif char == '\b': # if the character is backspace the last character is deleted
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else: # else, replace the characters with an asterisk
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

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, 'wb') as file:
            file.write(decrypted_data)

def opentxt():
    open('information.txt', 'x')

passwordfile = '#######.bin' # give the file that the password is in

while True:

    if os.path.exists(passwordfile): # if the file exists, read it from file and ask for the password

        storedpassword = read_password_from_file(passwordfile)

        passwordtoverify = masked_input("Enter the password to verify: ") # make sure the input is masked (replaced with asterisks)

        if verify_password(storedpassword, passwordtoverify): # verify passowrd
            print("Password is correct.")
            
            if find('information.txt', 'C:/Users/ericl/Documents/lab'):
                
                print('found it')

                get_key()

                key = load_key()

                file = 'information.txt'

                encrypt(file, key)
                
                break

            else:
                print('sdhufdshdflih')
            
        else:
            print("Password is incorrect.")
    else:
        newpassword = input("Enter a new password: ") # if the file isnt found, make a new one
        hashedpassword = hash_password(newpassword) # hash it

        save_password_to_file(hashedpassword, passwordfile) # make a new file, put the password (encrypted) into the file
        print("Password saved.")
