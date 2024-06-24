def factorial():
    n = int(input('Enter a positive integer: '))
    equation = '1'
    result = 1

    for i in range(2, n + 1):
        equation = equation + '*' + str(i)

    for i in range(2, n + 1):
        result *= i

    print(f'So {n}! would be ... {equation} = {result}')

factorial()