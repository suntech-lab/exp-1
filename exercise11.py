import random

def pass_gen():

    password_list = []

    while len(password_list) < random.randint(7, 11):
        password_list.append(chr(random.randint(33, 127)))
        password = ''.join(password_list)
        
    return password
                        
print(pass_gen())