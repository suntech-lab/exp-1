import random

def pass_gen():

    password_list = []

    while len(password_list) < 100:
        password_list.append(chr(random.randint(33, 127)))
        password = ''.join(password_list)
        
    return password
                        
print(pass_gen())