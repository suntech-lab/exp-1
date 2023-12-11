def evaluate(a):
    try:
        result = eval(a)
    except Exception as e:
        print(f'Error: {e}')
        return
    return result

def add(num1, num2):
    evaluate
    print(f'{num1} + {num2} = {num1 + num2}')

def sub(num1, num2):
    print(f'{num1} - {num2} = {num1 - num2}')

def multiply(num1, num2):
    print(f'{num1} * {num2} = {num1 * num2}')

def divide(num1, num2):
    print(f'{num1} / {num2} = {num1 / num2}')

def mod(num1, num2):
    print(f'{num1} % {num2} = {num1 % num2}')

def gcd(num1, num2):
    og_num1 = num1
    og_num2 = num2
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    print(f'the gcd of {og_num1} and {og_num2} = {num1}')

def lcm(num1, num2):
    og_num1 = num1
    og_num2 = num2
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    solution = (og_num1 * og_num2) // num1
    print(f"The lcm of {og_num1} and {og_num2} is: {solution}")

def power(num1, num2):
    if str.isnumeric(num1 ** num2) == True:
        print(f'{num1} ** {num2} = {float(num1) ** float(num2)}')
    else:
        print('sorry, this results in a complex number.')

def factorial(num1):
    if num1 == 0 or num1 == 1:
        return 1
    else:
        result = 1
        for i in range(2, num1 + 1):
            result *= i
        print(f'the factorial of {num1} = {result}')

def sqrt(num1):
    print(f'the square root of {num1} = {eval(num1) ** (1/2)}')



operation = int(input('''
1 for addition
2 for subtration
3 for multiplication
4 for division
5 for MOD
6 for GCD
7 for LCM
8 for exponents
9 for factorial
10 for square root
: '''))
while 1 > operation < 11 or operation != type(int):
    print('rerun the code, next time, choose one of the actual options please.')
    break
if operation == 1:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            add(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 2:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            sub(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 3:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            multiply(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 4:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            divide(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 5:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            mod(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 6:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            gcd(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 7:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            lcm(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 8:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            power(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated. please input something that is a number')
    else:
        print(f'input cannot be evaluated. please input something that is a number')
if operation == 9:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        if eval(num1) < 0:
            print(f'{num1} is a negative number, and cannot be evaluated')
        elif float.is_integer(float(num1)) == False:
            print(f'{num1} is a decimal, and thus cannot be evaluated')
        else:
            factorial(eval(num1))
    else:
        print('input cannot be evaluated. please input something that is a number')
if operation == 10:
    num1 = (input('your number: '))
    result = evaluate(num1)
    if result:
        if eval(num1) < 0:
            print(f'{num1} is a negative number. it has an imaginary root: {eval(num1) ** (1/2)}')
        else:
            sqrt(num1)
    else:
        print('input cannot be evaluated')
