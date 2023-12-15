
# calculates the inputted expression, prints error if it cannot
def validate_input(x):

    # tries to evaluate the x, the user input
    try:
        n = eval(x)

    # if it cant, it prints an error
    except Exception as error:
        print(error)
        return
    
    # gives the evaluated input back as n
    return n

# adds two numbers together, one of the simplest functions
def add():
    
    # ask user for input
    print('enter an integer, float, or expression')
    num1 = input()
    
    # validates input
    num1 = validate_input(num1)
    if not num1:
        return
    
    # ask user for second input
    print('enter your second integer, float, or expression')
    num2 = input()

    # validate second input
    num2 = validate_input(num2)

    # if num2 is not valid, return
    if not num2:
        return
    
    # once all of the inputs are validated, it does the actual operation
    print(f'result: {num1} + {num2} = {num1 + num2}')

# subtracts two numbers, again one of the simplest functions
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
    
    print(f'result: {num1} - {num2} = {num1 - num2}')

# again, one of the simplest functions, it multiplies two numbers
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
    
    print(f'result: {num1} * {num2} = {num1 * num2}')

# divides two numbers, makes sure that it cant divide by zero
def divide():

    # asks for first input, can be any integer, float, or expression
    print('enter an integer, float, or expression')
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    # asks for the second input
    print('enter your second integer, float, or expression that does not represent or equal to zero.')
    num2 = input()

    # validates it as if it were any other input
    num2 = validate_input(num2)

    # this time, the second input may not equal zero. if it does, it prints a request to enter it again
    while num2 == 0:
        print('num2 is equal to or represents zero, please input another number.')
        num2 = input()

        # validates the new input
        num2 = validate_input(num2)
    
    if not num2:
        return
    
    print(f'result: {num1} / {num2} = {num1 / num2}')

# mods the two inputted numbers so long as the second one is not zero.
def mod():

    print('enter an integer, float, or expression')
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    # enter the second input, like any other function
    print('enter your second integer, float, or expression')
    num2 = input()
    num2 = validate_input(num2)

    # this time, the second input may not equal zero. if it does, it prints a request to enter it again
    while num2 == 0:
        print('num2 is equal to or represents zero, please input another number.')
        num2 = input()

        # validates the new input
        num2 = validate_input(num2)

    if not num2:
        return
    
    print(f'result: {num1} % {num2} = {num1 % num2}')

# finds the greatest common divisor of two numbers
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
    
    # keeps the original inputs, because it modifies them later
    og_num1 = num1
    og_num2 = num2

    # modifies the inputs to find the gcd with euclid's algorithm
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    # prints the original inputs, and then the number that was converted to the gcd
    print(f'result: the gcd of {og_num1} and {og_num2} = {num1}')

# gets the lowest common multiple of two user inputs
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
    
    # finds the gcd between the two numbers
    og_num1 = num1
    og_num2 = num2
    while num2 != 0:
        num1, num2 = num2, num1 % num2

    # floor divides the product of the original inputs by the gcd to find the lcm
    solution = (og_num1 * og_num2) // num1

    # prints the solution
    print(f"result: The lcm of {og_num1} and {og_num2} is: {solution}")

# raises the first input to the power of the second
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
    
    # prevents outputting complex numbers
    if type(num1 ** num2) == complex:
        print('complex number, not available')
    
    # if there is no complex number output, print the answer.
    else:
        print(f'result: {num1} ** {num2} = {num1 ** num2}')


# finds the factorial of a positive integer
def factorial():

    # the factorial of negative numbers are complex
    print('enter a positive integer')
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    if num1 == 0 or num1 == 1: # base case for 0 and 1
        return 1
    
    # if the inputted number is less than 0, it is a negative, and the result is complex
    elif num1 < 0:
        print('complex number, not available.')
        return

    # prevent factorial for decimal numbers
    elif type(num1) == float:
        print('factorial does not exist for decimal numbers')

    # if it is larger than 0, proceed with calculating the factorial
    else:

        # multiply each number from 2 to the input
        result = 1

        # 1 is added to the first input because it is exclusive
        for i in range(2, num1 + 1):
            result *= i

        # print the result
        print(f'result: the factorial of {num1} = {result}')

# square root the input, or raise it to the power of 1/2
def sqrt():

    print('enter an integer, float, or expression')
    num1 = input()

    num1 = validate_input(num1)
    if not num1:
        return
    
    # cannot square negative numbers, so print that complex numbers are not available
    if num1 < 0:
        print('complex number, not available.')

    # otherwise if it is not a complex number, proceed with calculating it
    else:
        print(f'result: the square root of {num1} = {num1 ** (1/2)}')

# the 'menu' that shows the user what can be inputted
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
    {'operation': '10', 'description': 'square root', 'func': sqrt}
]

# start the calculator
def start():

    # print the schema
    for op in operation_schema:
        print(f"enter {op['operation']} for {op['description']}")

    # the user chooses an operation from the schema
    user_op_choice = input('please enter here:')

    # find the operation that is associated with the number/option that the user chooses
    for op in operation_schema:
        if user_op_choice == str(op['operation']):

            # execute the function
            op['func']()
            break

    # if they dont enter a valid choice, tell them to re-enter the choice
    else:
        print('invalid input, please rerun the code and put in a valid input.')

# exit the program if stop is executed
def stop():
    exit()

# asks the user if it should start/continue or stop
start_schema = [
    {'option': 'yes', 'purpose': 'start/continue', 'function': start},
    {'option': 'no', 'purpose': 'stop', 'function': stop}
]

# first thing that the user sees
def menu():

    for opt in start_schema:
        print(f"\nenter {opt['option']} to {opt['purpose']}")

    user_option_choice = input('\nplease enter here:')

    for opt in start_schema:
        if user_option_choice == str(opt['option']):

            opt['function']()
            break

while True:
    menu()