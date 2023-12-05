import math

def is_it_prime(prime_number):
    if prime_number <= 1:
        print('False')
        return

    for x in range(2, int(math.sqrt(prime_number)) + 1):
        if prime_number % x == 0:
            print('False')
            return

    print('True')

prime_number = int(input('what is your number: '))
is_it_prime(prime_number)