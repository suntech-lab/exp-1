def validate_input(input): # calculates the inputted expression, prints error if it cannot

    try: # tries to evaluate the x, the user input
        num = eval(input)

    except Exception as error: # if it cant, it prints an error
        print(error)
        return
    
    return num # gives the evaluated input back as num

def add(): # adds two numbers together, one of the simplest functions
    
    print('enter an integer, float, or expression') # ask user for input
    num1 = input()
    
    num1 = validate_input(num1) # validates input
    if not num1:
        return
    
    print('enter your second integer, float, or expression') # ask user for second input
    num2 = input()

    num2 = validate_input(num2) # validate second input

    if not num2: # if num2 is not valid, return
        return
    
    print(f'result: {num1} + {num2} = {num1 + num2}') # once all of the inputs are validated, it does the actual operation

def sub(): # subtracts two numbers, again one of the simplest functions

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
    
    print(f'result: {num1} - {num2} = {num1 - num2}')

def multiply(): # again, one of the simplest functions, it multiplies two numbers

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
    
    print(f'result: {num1} * {num2} = {num1 * num2}')

def divide(): # divides two numbers, makes sure that it cant divide by zero

    print('enter an integer, float, or expression') # asks for first input, can be any integer, float, or expression
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    print('enter your second integer, float, or expression that does not represent or equal to zero.') # asks for the second input

    num2 = input()

    num2 = validate_input(num2) # validates it as if it were any other input

    while num2 == 0: # this time, the second input may not equal zero. if it does, it prints a request to enter it again
        print('num2 is equal to or represents zero, divide by zero error')
        break
    
    if not num2:
        return
    
    print(f'result: {num1} / {num2} = {num1 / num2}')

def mod(): # mods the two inputted numbers so long as the second one is not zero.

    print('enter an integer, float, or expression')
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    print('enter your second integer, float, or expression') # enter the second input, like any other function
    num2 = input()
    num2 = validate_input(num2)

    while num2 == 0: # this time, the second input may not equal zero. if it does, it prints a request to enter it again
        print('num2 is equal to or represents zero, please input another number.')
        num2 = input()

        num2 = validate_input(num2) # validates the new input

    if not num2:
        return
    
    print(f'result: {num1} % {num2} = {num1 % num2}')

def gcd(): # finds the greatest common divisor of two numbers

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
    og_num2 = num2 # keeps the original inputs, because it modifies them later

    while num2 != 0:
        num1, num2 = num2, num1 % num2 # modifies the inputs to find the gcd with euclid's algorithm

    print(f'result: the gcd of {og_num1} and {og_num2} = {num1}') # prints the original inputs, and then the number that was converted to the gcd

def lcm(): # gets the lowest common multiple of two user inputs

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
        num1, num2 = num2, num1 % num2 # finds the gcd between the two numbers

    solution = (og_num1 * og_num2) // num1 # floor divides the product of the original inputs by the gcd to find the lcm

    print(f"result: The lcm of {og_num1} and {og_num2} is: {solution}") # prints the solution

def power(): # raises the first input to the power of the second

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
    
    if type((num1) ** (num2)) == complex: # prevents outputting complex numbers
        print('complex number, not available')
    
    else: # if there is no complex number output, print the answer
        print(f'result: {num1} ** {num2} = {num1 ** num2}')

def factorial(): # finds the factorial of a positive integer

    print('enter a positive integer') # the factorial of negative numbers are complex
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    if num1 == 0 or num1 == 1: # base case for 0 and 1
        return 1
    
    elif num1 < 0: # if the inputted number is less than 0, it is a negative, and the result is complex
        print('complex number, not available.')
        return

    elif type(num1) == float: # prevent factorial for decimal numbers
        print('factorial does not exist for decimal numbers')

    else: # if it is larger than 0, proceed with calculating the factorial

        result = 1

        for i in range(2, num1 + 1): # 1 is added to the first input because it is exclusive
            result *= i

        print(f'result: the factorial of {num1} = {result}') # print the result

def sqrt(): # square root the input, or raise it to the power of 1/2

    print('enter an integer, float, or expression')
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    if num1 < 0: # cannot square negative numbers, so print that complex numbers are not available
        print('complex number, not available.')

    else: # otherwise if it is not a complex number, proceed with calculating it
        print(f'result: the square root of {num1} = {num1 ** (1/2)}')

operation_schema = [ # the 'menu' that shows the user what can be inputted
    {'operation': '1', 'description': 'addition', 'func': add},
    {'operation': '2', 'description': 'subtraction', 'func': sub},
    {'operation': '3', 'description': 'multiplication', 'func': multiply},
    {'operation': '4', 'description': 'division', 'func': divide},
    {'operation': '5', 'description': 'MOD', 'func': mod},
    {'operation': '6', 'description': 'GCD', 'func': gcd},
    {'operation': '7', 'description': 'LCM', 'func': lcm},
    {'operation': '8', 'description': 'exponents', 'func': power},
    {'operation': '9', 'description': 'factorial', 'func': factorial},
    {'operation': '10', 'description': 'square root', 'func': sqrt}
]

# start the calculator
def start():

    # print the schema
    for op in operation_schema:
        print(f"enter {op['operation']} for {op['description']}")

    # the user chooses an operation from the schema
    user_op_choice = input('\nplease enter here: ')

    # find the operation that is associated with the number/option that the user chooses
    for op in operation_schema:
        if user_op_choice == str(op['operation']):

            # execute the function
            op['func']()
            break

    # if they dont enter a valid choice, tell them to re-enter the choice
    else:
        print('invalid input, please put in a valid input.')

# exit the program if stop is executed
def stop():
    exit()

# asks the user if it should start/continue or stop
start_schema = [
    {'option': 'yes', 'purpose': 'start/continue the calculator', 'function': start},
    {'option': 'no', 'purpose': 'stop the calculator', 'function': stop}
]

# first thing that the user sees
def menu():

    for opt in start_schema:
        print(f"\nenter '{opt['option']}' to {opt['purpose']}")

    user_option_choice = input('\nplease enter here: ')

    for opt in start_schema:
        if user_option_choice == str(opt['option']):

            opt['function']()
            break

while True:
    menu()