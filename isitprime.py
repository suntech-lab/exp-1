import math

def is_it_prime(prime_number):
    if prime_number <= 1:
        print('Not a prime number')
        return

    for x in range(2, int(math.sqrt(prime_number)) + 1):
        if prime_number % x == 0:
            print('Not a prime number')
            return

    print('It is a prime number')

prime_number = int(input('What is your number: '))
is_it_prime(prime_number)