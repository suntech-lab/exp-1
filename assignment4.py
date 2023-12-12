def evaluate(a):
    try:
        result = eval(a)
    except Exception as e:
        print(f'Error: {e}')
        return
    return result

def validate_input(x):
    try:
        n = eval(x)
    except Exception as error:
        print(error)
        return
    return n

def add():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    print(f'{num1} + {num2} = {num1 + num2}')

def sub():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    print(f'{num1} - {num2} = {num1 - num2}')

def multiply():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    print(f'{num1} * {num2} = {num1 * num2}')

def divide():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    print(f'{num1} / {num2} = {num1 / num2}')

def mod():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    print(f'{num1} % {num2} = {num1 % num2}')

def gcd():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    og_num1 = num1
    og_num2 = num2
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    print(f'the gcd of {og_num1} and {og_num2} = {num1}')

def lcm():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    og_num1 = num1
    og_num2 = num2
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    solution = (og_num1 * og_num2) // num1
    print(f"The lcm of {og_num1} and {og_num2} is: {solution}")

def power():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)
    if not num2:
        return
    if type(num1 ** num2) == complex:
        print('complex number, not available')
    else:
        print(f'{num1} ** {num2} = {num1 ** num2}')

def factorial():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    if num1 == 0 or num1 == 1:
        return 1
    elif num1 < 0:
        print('complex number, not available.')
    else:
        result = 1
        for i in range(2, num1 + 1):
            result *= i
        print(f'the factorial of {num1} = {result}')

def sqrt():
    print('enter an integer, float, or expression')
    num1 = input()
    num1 = validate_input(num1)
    if not num1:
        return
    if num1 < 0:
        print('complex number, not available.')
    else:
        print(f'the square root of {num1} = {num1 ** (1/2)}')

operation_schema = [
    {'operation': '1', 'description': 'addition', 'func': add},
    {'operation': '2', 'description': 'subtraction', 'func': sub},
    {'operation': '3', 'description': 'multiplication', 'func': multiply},
    {'operation': '4', 'description': 'division', 'func': divide},
    {'operation': '5', 'description': 'MOD', 'func': mod},
    {'operation': '6', 'description': 'GCD', 'func': gcd},
    {'operation': '7', 'description': 'LCM', 'func': lcm},
    {'operation': '8', 'description': 'exponents', 'func': power},
    {'operation': '9', 'description': 'factorial', 'func': factorial},
    {'operation': '10', 'description': 'square root', 'func': sqrt},
]

for op in operation_schema:
    print(f"enter {op['operation']} for {op['description']}")

user_op_choice = input()
for op in operation_schema:
    if user_op_choice == str(op['operation']):
        op['func']()
        break
else:
    print('invalid input, please rerun the code and put in a valid input.')

"""
while True:
    try:
        operation = int(input('''
enter 1 for addition
enter 2 for subtration
enter 3 for multiplication
enter 4 for division
enter 5 for MOD
enter 6 for GCD
enter 7 for LCM
enter 8 for exponents
enter 9 for factorial
enter 10 for square root
: '''))
    except Exception as e:
        print('try again')
    if operation == type(int) and operation >= 1 and operation <= 10:
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
"""