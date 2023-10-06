import random

def get_n():
    a = 0
    b = 0
    while a == b:
        a = int(random.randint(1,100000000000000))
        b = int(random.randint(1,100000000000000))
    c = (a**2 + b**2)**(1 / 2)
    n = 100 * (a / c)
    return n

sum = 0
count = 0
while count < 10000000:
    sum += get_n()
    count += 1

print(sum / 10000000)
