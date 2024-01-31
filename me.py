import hashlib
import os
import msvcrt

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(64)  # Generate a random salt if not provided
    hash_bytes = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + hash_bytes

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]  # Extract the salt from the stored password
    stored_hash = stored_password[64:]  # Extract the hash from the stored password
    provided_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode('utf-8'), salt, 100000)
    return stored_hash == provided_hash

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

# Check if the password file exists
password_file = '#######.bin'
if os.path.exists(password_file):
    # Read the stored password from the file
    stored_password = read_password_from_file(password_file)

    # Get the password to verify from the user
    password_to_verify = masked_input("Enter the password to verify: ")

    # Verify the password
    if verify_password(stored_password, password_to_verify):
        print("Password is correct.")
    else:
        print("Password is incorrect.")
else:
    # If the password file doesn't exist, prompt the user to create a new password
    new_password = input("Enter a new password: ")
    hashed_password = hash_password(new_password)
    # Save the hashed password to the file
    save_password_to_file(hashed_password, password_file)
    print("Password saved.")
