import math

def prime_number_generator():
    prime_number = 10000000000000000
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(prime_number) + 1)):
            if prime_number % x == 0: 
                isprime = False
                break 
        if isprime:
            prime_number = prime_number + 1
        prime_number += 1

prime_number_generator()