import math

x = str(input('functions (limited) or arithmetic operations: '))

if x == 'arithmetic operations':
    num1 = complex(input('enter the first number: '))
    op = str(input('enter the operation: '))
    num2 = complex(input('enter the second number: '))

    if op == "+":
        print(num1, "+", num2, "is", num1 + num2)
    if op == "-":       
        print(num1, "-", num2, "is", num1 - num2)
    if op == "/":
        print(num1, "/", num2, "is", num1 / num2)
    if op == "*":
        print(num1, "*", num2, "is", num1 * num2)
    if op == "%":
        print(num1, "%", num2, "is", num1 % num2)
    if op == "//":
        print(num1, "//", num2, "is", num1 // num2)
    if op == "**":
        print(num1, "**", num2, "is", num1 ** num2)

if x == 'functions':
    op = str(input('factorial, delta, square root, or absolute value: '))

    if op == 'factorial':
        factorial = 1
        num1 = int(input('what number do you want the factorial of? (has to be a positive integer): '))
        for i in range(1, num1 + 1):
            factorial = factorial * i
        print('the factorial of', num1, 'is', factorial)
    if op == 'delta':
        delta = 0
        num1 = int(input('what do you want the delta of (has to be a positive integer): '))
        for i in range(1, num1 + 1):
            delta = delta + i
        print('the delta of', num1, 'is', delta)
    if op == 'square root':
        num1 = complex(input('what do you want the square root of: '))
        print(num1 ** (1/2))
    if op == 'absolute value':
        num1 = float(input('what number do you want to absolute value of? (floats only): '))
        if num1 > 0:
            print(num1)
        if num1 < 0:
            print(num1 * (-1))

