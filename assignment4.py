import math

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
    print(f'{num1} ** {num2} = {num1 ** num2}')

def factorial(num1):
    if type(num1) == float:
        if float.is_integer(num1) == True:
            print(f'the factorial of {num1} = {math.factorial(num1)}')
        else:
            print(f'{num1} is not an integer')
    else:
        print(f'the factorial of {num1} = {math.factorial(num1)}')

def sqrt(num1):
    print(f'the square root of {num1} = {math.sqrt(eval(num1))}')



operation = int(input('enter \'1\' for addition \nenter \'2\' for subtraction \nenter \'3\' for multiplication \nenter \'4\' for division \nenter \'5\' for MOD \nenter \'6\' for GCD \nenter \'7\' for LCM \nenter \'8\' for power \nenter \'9\' for factorial \nenter \'10\' for square root \n: '))
if operation == 1:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            add(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 2:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            sub(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 3:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            multiply(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 4:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            divide(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 5:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            mod(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 6:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            gcd(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 7:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            lcm(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 8:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        num2 = (input('enter your second number: '))
        result = evaluate(num2)
        if result:
            power(eval(num1), eval(num2))
        else:
            print(f'input cannot be evaluated')
    else:
        print(f'input cannot be evaluated')
if operation == 9:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        if eval(num1) < 0:
            print(f'{num1} is a negative number, and cannot be evaluated')
        elif num1 == type(float):
            print(f'{num1} is a decimal, and thus cannot be evaluated')
        else:
            factorial(eval(num1))
    else:
            print('input cannot be evaluated')
if operation == 10:
    num1 = (input('enter your number: '))
    result = evaluate(num1)
    if result:
        if eval(num1) < 0:
            print(f'{num1} is a negative number. it has an imaginary root: {eval(num1) ** (1/2)}')
        else:
            sqrt(num1)
    else:
        print('input cannot be evaluated')
