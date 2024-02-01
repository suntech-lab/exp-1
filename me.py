import hashlib
import os
import msvcrt

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(64)
    hashbytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 500000)
    return salt + hashbytes

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

def masked_input(prompt):
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


passwordfile = '#######.bin'
if os.path.exists(passwordfile):
    
    storedpassword = read_password_from_file(passwordfile)

    passwordtoverify = masked_input("Enter the password to verify: ")

    if verify_password(storedpassword, passwordtoverify):
        print("Password is correct.")
    else:
        print("Password is incorrect.")
else:
    newpassword = input("Enter a new password: ")
    hashedpassword = hash_password(newpassword)

    save_password_to_file(hashedpassword, passwordfile)
    print("Password saved.")
