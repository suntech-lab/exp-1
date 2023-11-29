# define what recursion is
'''
Recursion is a process in which a function calls itself, called recursive functions.
'''

# give the formula for fibonacci's sequence and define what it means
'''
The formula for Fibonacci's sequence is f[n] = f[n-1] + f[n-2].
This means that the newest number in the sequence is the sum of the last 2.
The value of the largest index is the sum of one less than the largest and 2 less than the largest.
'''

# what is the golden ratio
'''
The golden ratio is the ratio of two consecutive numbers in the Fibonacci sequence.
The larger the numbers are, the more precise the ratio is.
Usually written to three decimal places, 1.618.
'''

# implement in python a recursive definition for fibonacci sequence and dis-allow negative n values (n > 1)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

n = 0

last_index = 9

while n < last_index:
    print(fib(n))
    n += 1