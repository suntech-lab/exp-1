def gen_fib():

    last_index = int(input('How many digits of the Fibonacci sequence do you want?: '))

    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

    n = 1
    sequence = str(fib(0))

    while n < last_index:
        sequence = sequence + ', ' + str(fib(n))
        n += 1

    print(f'So Fibonacci({last_index}) would print the first {last_index} digits of this sequence ...\n\nOutput: {sequence}')

gen_fib()